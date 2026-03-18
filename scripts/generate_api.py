import sys
import re
from bs4 import BeautifulSoup

def normalize_type(raw_type):
    t = raw_type.lower().strip()
    if t == 'string':
        return 'str'
    if t in ('int', 'integer'):
        return 'int'
    if t in ('float', 'double', 'number'):
        return 'float'
    if t in ('bool', 'boolean'):
        return 'bool'
    if t == 'array':
        return 'list[dict[str, Any]]'
    if t in ('date', 'datetime'):
        return 'str'
    return 'Any'

def parse_table(table_node):
    rows = []
    for tr in table_node.find_all('tr'):
        cells = [c.get_text().strip() for c in tr.find_all(['th', 'td'])]
        if not cells:
            continue
        rows.append(cells)

    if not rows: return []

    headers = [h.lower() for h in rows[0]]
    if 'változó' not in headers:
        return []

    idx_name = headers.index('változó')
    idx_type = headers.index('típus') if 'típus' in headers else -1
    idx_req = headers.index('kötelező') if 'kötelező' in headers else -1

    parsed_fields = []

    for row in rows[1:]:
        if len(row) <= idx_name:
            continue

        name = row[idx_name]
        # Remove any leading strange chars like dashes or greater than from name: "- invoice_start" -> "invoice_start"
        name = re.sub(r'^[\s\->]+', '', name)

        if not name or '[' in name or ']' in name:
            continue

        t_type = row[idx_type] if idx_type != -1 and len(row) > idx_type else 'string'
        req_val = row[idx_req] if idx_req != -1 and len(row) > idx_req else ''

        # Determine required: 'R', 'R*', 'O/R', etc. We'll be conservative and say R is required.
        is_req = req_val.upper().startswith('R') and 'O' not in req_val.upper()

        parsed_fields.append({
            'name': name,
            'type': normalize_type(t_type),
            'required': is_req
        })

    return parsed_fields

def extract_endpoints(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'lxml')
    endpoints = []

    for h3 in soup.find_all('h3'):
        text = h3.get_text().strip()
        endpoint_name = text.split()[0].strip()

        if not endpoint_name or not endpoint_name.isalnum():
             continue

        node = h3.next_sibling
        tables = []

        while node and getattr(node, 'name', '') not in ('h2', 'h3'):
            if getattr(node, 'name', '') == 'table':
                parsed = parse_table(node)
                if parsed:
                    tables.append(parsed)
            node = node.next_sibling

        if len(tables) >= 2:
            req_table = tables[0]
            resp_table = tables[1]

            # Remove base credentials
            req_table = [f for f in req_table if f['name'] not in ('uid', 'password', 'block')]

            # Deduplicate fields
            seen = set()
            dedup_req = []
            for f in req_table:
                if f['name'] not in seen:
                    seen.add(f['name'])
                    dedup_req.append(f)

            seen = set()
            dedup_resp = []
            for f in resp_table:
                if f['name'] not in seen:
                    seen.add(f['name'])
                    dedup_resp.append(f)

            endpoints.append({
                'name': endpoint_name,
                'request': dedup_req,
                'response': dedup_resp
            })

    return endpoints

def generate_python(endpoints, output_file):
    with open(output_file, 'w') as f:
        f.write("from typing import Any, Optional\n")
        f.write("from dataclasses import dataclass, asdict\n")
        f.write("from .client import OnlineSzamlazoClient\n\n")

        # Write Dataclasses
        for ep in endpoints:
            # We enforce title case properly for things like install -> Install
            req_name = ep['name'][0].upper() + ep['name'][1:] + 'Request'
            resp_name = ep['name'][0].upper() + ep['name'][1:] + 'Response'

            # Define request class
            f.write(f"@dataclass\nclass {req_name}:\n")
            if not ep['request']:
                f.write("    pass\n")
            else:
                # Need to order fields so required (non-default) ones come before optional (default) ones
                req_fields = [f for f in ep['request'] if f['required']]
                opt_fields = [f for f in ep['request'] if not f['required']]
                ordered_fields = req_fields + opt_fields
                for field in ordered_fields:
                    py_name = field['name']
                    if py_name in ('from', 'import', 'pass', 'type', 'id', 'def', 'class', 'global', 'list', 'dict'):
                        py_name += '_'

                    # Some spec params have dots in them (e.g. conn.host) which are invalid python identifiers
                    py_name = py_name.replace('.', '_').replace('-', '_')

                    if field['required']:
                        f.write(f"    {py_name}: {field['type']}\n")
                    else:
                        f.write(f"    {py_name}: Optional[{field['type']}] = None\n")
            f.write("\n")

            # Define response class
            f.write(f"@dataclass\nclass {resp_name}:\n")
            if not ep['response']:
                f.write("    pass\n")
            else:
                for field in ep['response']:
                    py_name = field['name']
                    # 'list' is a built-in type, we should rename it so it doesn't shadow the type alias
                    if py_name in ('from', 'import', 'pass', 'type', 'id', 'def', 'class', 'global', 'list', 'dict'):
                        py_name += '_'
                    py_name = py_name.replace('.', '_').replace('-', '_')

                    f.write(f"    {py_name}: Optional[{field['type']}] = None\n")
            f.write("\n")

        # Write API Client wrapper
        f.write("class SzamlaiktatoAPI:\n")
        f.write("    def __init__(self, client: OnlineSzamlazoClient):\n")
        f.write("        self.client = client\n\n")

        for ep in endpoints:
            req_name = ep['name'][0].upper() + ep['name'][1:] + 'Request'
            resp_name = ep['name'][0].upper() + ep['name'][1:] + 'Response'
            method_name = ep['name']

            # Only put request arg if there are any fields, but it's simpler to always accept it and default to None if empty
            if ep['request']:
                 f.write(f"    def {method_name}(self, request: {req_name}, skip_block: bool = False) -> {resp_name}:\n")
            else:
                 f.write(f"    def {method_name}(self, request: Optional[{req_name}] = None, skip_block: bool = False) -> {resp_name}:\n")

            f.write(f"        params = asdict(request) if request else {{}}\n")

            # Handle variable renaming mapping
            for field in ep['request']:
                py_name = field['name'].replace('.', '_').replace('-', '_')
                orig_name = field['name']
                if py_name in ('from', 'import', 'pass', 'type', 'id', 'def', 'class', 'global', 'list', 'dict'):
                    py_name += '_'

                if py_name != orig_name:
                    f.write(f"        if '{py_name}' in params:\n")
                    f.write(f"            params['{orig_name}'] = params.pop('{py_name}')\n")

            f.write(f"        data = self.client._call('{method_name}', params, skip_block=skip_block)\n")

            # Response mappings
            for field in ep['response']:
                py_name = field['name'].replace('.', '_').replace('-', '_')
                orig_name = field['name']
                if py_name in ('from', 'import', 'pass', 'type', 'id', 'def', 'class', 'global', 'list', 'dict'):
                    py_name += '_'
                if py_name != orig_name:
                    f.write(f"        if '{orig_name}' in data:\n")
                    f.write(f"            data['{py_name}'] = data.pop('{orig_name}')\n")

            f.write(f"        valid_keys = {resp_name}.__dataclass_fields__.keys()\n")
            f.write(f"        filtered_data = {{k: v for k, v in data.items() if k in valid_keys}}\n")
            f.write(f"        return {resp_name}(**filtered_data)\n\n")

if __name__ == '__main__':
    endpoints = extract_endpoints(sys.argv[1])
    generate_python(endpoints, sys.argv[2])

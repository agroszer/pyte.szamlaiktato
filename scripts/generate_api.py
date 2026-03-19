import sys
import re
from bs4 import BeautifulSoup


def normalize_type(raw_type):
    t = raw_type.lower().strip()
    if t == "string":
        return "str"
    if t in ("int", "integer"):
        return "int"
    if t in ("float", "double", "number"):
        return "float"
    if t in ("bool", "boolean"):
        return "bool"
    if t == "array":
        return "list[dict[str, Any]]"
    if t in ("date", "datetime"):
        return "str"
    return "Any"


def parse_table(table_node):
    rows = []
    for tr in table_node.find_all("tr"):
        cells = [c.get_text().strip() for c in tr.find_all(["th", "td"])]
        if not cells:
            continue
        rows.append(cells)

    if not rows:
        return []

    headers = [h.lower() for h in rows[0]]
    if "változó" not in headers:
        return []

    idx_name = headers.index("változó")
    idx_type = headers.index("típus") if "típus" in headers else -1
    idx_req = headers.index("kötelező") if "kötelező" in headers else -1

    parsed_fields = []

    for row in rows[1:]:
        if len(row) <= idx_name:
            continue

        name = row[idx_name]
        name = re.sub(r"^[\s\->]+", "", name)

        if not name or "[" in name or "]" in name:
            continue

        t_type = row[idx_type] if idx_type != -1 and len(row) > idx_type else "string"
        req_val = row[idx_req] if idx_req != -1 and len(row) > idx_req else ""

        is_req = req_val.upper().startswith("R") and "O" not in req_val.upper()

        parsed_fields.append(
            {"name": name, "type": normalize_type(t_type), "required": is_req}
        )

    return parsed_fields


def extract_endpoints(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "lxml")
    endpoints = []

    for h3 in soup.find_all("h3"):
        text = h3.get_text().strip()
        endpoint_name = text.split()[0].strip()

        if not endpoint_name or not endpoint_name.isalnum():
            continue

        node = h3.next_sibling
        tables = []

        while node and getattr(node, "name", "") not in ("h2", "h3"):
            if getattr(node, "name", "") == "table":
                parsed = parse_table(node)
                if parsed:
                    tables.append(parsed)
            node = node.next_sibling

        if len(tables) >= 2:
            req_table = tables[0]
            resp_table = tables[1]

            # Remove base credentials
            req_table = [
                f for f in req_table if f["name"] not in ("uid", "password", "block")
            ]

            # Deduplicate fields
            seen = set()
            dedup_req = []
            for f in req_table:
                if f["name"] not in seen:
                    seen.add(f["name"])
                    dedup_req.append(f)

            seen = set()
            dedup_resp = []
            for f in resp_table:
                if f["name"] not in seen:
                    seen.add(f["name"])
                    dedup_resp.append(f)

            endpoints.append(
                {
                    "name": endpoint_name,
                    "request": dedup_req,
                    "response": dedup_resp,
                }
            )

    return endpoints


def generate_python(endpoints, output_file):
    with open(output_file, "w") as f:
        f.write("from typing import Any, Optional\n")
        f.write("from dataclasses import dataclass, asdict\n")
        f.write("from .client import OnlineSzamlazoClient\n\n")

        for ep in endpoints:
            req_name = ep["name"][0].upper() + ep["name"][1:] + "Request"
            resp_name = ep["name"][0].upper() + ep["name"][1:] + "Response"

            f.write(f"@dataclass\nclass {req_name}:\n")
            if not ep["request"]:
                f.write("    pass\n")
            else:
                req_fields = [fi for fi in ep["request"] if fi["required"]]
                opt_fields = [fi for fi in ep["request"] if not fi["required"]]
                ordered_fields = req_fields + opt_fields
                for field in ordered_fields:
                    py_name = field["name"]
                    reserved = (
                        "from",
                        "import",
                        "pass",
                        "type",
                        "id",
                        "def",
                        "class",
                        "global",
                        "list",
                        "dict",
                    )
                    if py_name in reserved:
                        py_name += "_"

                    py_name = py_name.replace(".", "_").replace("-", "_")

                    if field["required"]:
                        f.write(f"    {py_name}: {field['type']}\n")
                    else:
                        f.write(f"    {py_name}: Optional[{field['type']}] = None\n")
            f.write("\n")

            f.write(f"@dataclass\nclass {resp_name}:\n")
            if not ep["response"]:
                f.write("    pass\n")
            else:
                for field in ep["response"]:
                    py_name = field["name"]
                    reserved = (
                        "from",
                        "import",
                        "pass",
                        "type",
                        "id",
                        "def",
                        "class",
                        "global",
                        "list",
                        "dict",
                    )
                    if py_name in reserved:
                        py_name += "_"
                    py_name = py_name.replace(".", "_").replace("-", "_")

                    f.write(f"    {py_name}: Optional[{field['type']}] = None\n")
            f.write("\n")

        f.write("class SzamlaiktatoAPI:\n")
        f.write("    def __init__(self, client: OnlineSzamlazoClient):\n")
        f.write("        self.client = client\n\n")

        for ep in endpoints:
            req_name = ep["name"][0].upper() + ep["name"][1:] + "Request"
            resp_name = ep["name"][0].upper() + ep["name"][1:] + "Response"
            method_name = ep["name"]

            if ep["request"]:
                sig = f"request: {req_name}, skip_block: bool = False"
            else:
                sig = f"request: Optional[{req_name}] = None, skip_block: bool = False"
            f.write(f"    def {method_name}(self, {sig}) -> {resp_name}:\n")
            f.write("        params = asdict(request) if request else {}\n")

            for field in ep["request"]:
                py_name = field["name"].replace(".", "_").replace("-", "_")
                orig_name = field["name"]
                reserved = (
                    "from",
                    "import",
                    "pass",
                    "type",
                    "id",
                    "def",
                    "class",
                    "global",
                    "list",
                    "dict",
                )
                if py_name in reserved:
                    py_name += "_"

                if py_name != orig_name:
                    f.write(f"        if '{py_name}' in params:\n")
                    f.write(
                        f"            params['{orig_name}'] = params.pop('{py_name}')\n"
                    )

            f.write(
                f"        data = self.client._call(\n"
                f"            '{method_name}', params, skip_block=skip_block\n"
                f"        )\n"
            )

            for field in ep["response"]:
                py_name = field["name"].replace(".", "_").replace("-", "_")
                orig_name = field["name"]
                reserved = (
                    "from",
                    "import",
                    "pass",
                    "type",
                    "id",
                    "def",
                    "class",
                    "global",
                    "list",
                    "dict",
                )
                if py_name in reserved:
                    py_name += "_"
                if py_name != orig_name:
                    f.write(f"        if '{orig_name}' in data:\n")
                    f.write(
                        f"            data['{py_name}'] = data.pop('{orig_name}')\n"
                    )

            f.write(f"        valid_keys = {resp_name}.__dataclass_fields__.keys()\n")
            f.write(
                "        filtered_data = {\n"
                "            k: v for k, v in data.items() if k in valid_keys\n"
                "        }\n"
            )
            f.write(f"        return {resp_name}(**filtered_data)\n\n")


if __name__ == "__main__":
    endpoints = extract_endpoints(sys.argv[1])
    generate_python(endpoints, sys.argv[2])

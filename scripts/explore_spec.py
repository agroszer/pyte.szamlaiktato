import sys
from bs4 import BeautifulSoup


def extract_tables(soup, endpoint_name):
    print(f"--- Endpoint: {endpoint_name} ---")

    # Find the h3 containing the endpoint name
    h3_tags = soup.find_all("h3")
    endpoint_h3 = None
    for h3 in h3_tags:
        text = h3.get_text().strip()
        # Ensure it matches the endpoint exactly
        if text.startswith(endpoint_name) and (
            len(text) == len(endpoint_name) or not text[len(endpoint_name)].isalnum()
        ):
            endpoint_h3 = h3
            break

    if not endpoint_h3:
        print("Not found")
        return

    # the parameter tables usually follow this h3 until the next h3 or h2
    node = endpoint_h3.next_sibling
    tables = []

    while node and getattr(node, "name", "") not in ("h2", "h3"):
        if node.name == "table":
            # extracting table rows
            table_data = []
            for tr in node.find_all("tr"):
                row = [td.get_text().strip() for td in tr.find_all(["th", "td"])]
                if row:
                    table_data.append(row)
            if table_data:
                tables.append(table_data)

        node = node.next_sibling

    print(f"Found {len(tables)} tables")
    for i, t in enumerate(tables):
        print(f" Table {i}: {t[0]}")  # headers
        if len(t) > 1:
            print(f"          {t[1]}")  # first row


def main():
    html_file = sys.argv[1]
    with open(html_file, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "lxml")
    extract_tables(soup, "customerAdd")
    extract_tables(soup, "customerList")
    extract_tables(soup, "invoiceAdd")


if __name__ == "__main__":
    main()

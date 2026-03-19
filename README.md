# pyte.szamlaiktato

A fully typed, Python 3.10+ REST API client for [Számlaiktató.hu](https://www.szamlaiktato.hu/) (Online Számlázó), automatically generated from their official API specifications.

## Features

- **Fully Typed:** All ~120 endpoints have complete `dataclass` definitions for both requests and responses. Mypy and IDEs like VSCode/PyCharm will give you perfect autocompletion and type checking.
- **REST/JSON only:** The client natively uses the JSON `POST` endpoints.
- **Automatic Credentials Injection:** Handles `uid`, `password`, and `block` payload injection seamlessly.

## Installation

You can install the package directly from PyPI (once published), or via source:

```bash
pip install pyte.szamlaiktato
```

Or clone the repository and install it:

```bash
pip install .
```

## Usage Example

```python
from pyte.szamlaiktato import OnlineSzamlazoClient, SzamlaiktatoAPI
from pyte.szamlaiktato.api import CustomerAddRequest

# Initialize the low-level client with your credentials
client = OnlineSzamlazoClient(
    api_url="https://api.szamlaiktato.hu/restServer",
    uid="YOUR_UID",
    password="YOUR_PASSWORD",
    block="YOUR_BLOCK"
)

# Instantiate the typed API wrapper
api = SzamlaiktatoAPI(client)

# Call an endpoint (e.g. customerAdd) using the typed Request dataclass
req = CustomerAddRequest(
    name="Test Customer Kft.",
    country="HU",
    postcode="1055",
    city="Budapest",
    street="Kossuth Lajos tér 1.",
    tax_number="12345678-1-41",
    email="billing@example.com"
)

try:
    response = api.customerAdd(req)
    print(f"Success! Status ID: {response.status_id}")
    print(f"New Customer Internal ID: {response.customer_id}")
except Exception as e:
    print(f"API Error: {e}")
```

## Error Handling

The client will automatically raise an `ApiError` if the returned `status_id` is 4000 or greater (indicating an API failure). You can catch this exception and access the `.status_id` or `.response` attribute to debug the issue.

```python
from pyte.szamlaiktato import ApiError

try:
    api.ping()
except ApiError as e:
    print(f"Failed with status: {e.status_id}")
    print(f"Full response: {e.response}")
```

## Development & Testing

This project uses `pytest`, `black`, `flake8` and `mypy` to enforce code quality.

1. Setup the environment:
   ```bash
   pip install -e . -r requirements-dev.txt
   ```

2. Run checks:
   ```bash
   black src/ tests/ scripts/
   flake8 src/ tests/ scripts/
   mypy src/
   pytest tests/
   ```

### Regenerating the API

If the official HTML spec changes, you can re-parse the endpoints by replacing the `spec/onlineszamlazo-api-hu-v7.58.html` file and running:

```bash
python3 scripts/generate_api.py spec/onlineszamlazo-api-hu-v7.58.html src/pyte/szamlaiktato/api.py
black src/pyte/szamlaiktato/api.py
```

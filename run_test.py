import pytest
import responses
from pyte.szamlaiktato.client import OnlineSzamlazoClient, ApiError
from pyte.szamlaiktato.api import SzamlaiktatoAPI, PingRequest

@responses.activate
def test_client_error():
    client = OnlineSzamlazoClient(
        "https://api.szamlaiktato.hu", "test_uid", "test_pass", "test_block", instance_id="123"
    )
    api = SzamlaiktatoAPI(client)

    responses.add(
        responses.POST,
        "https://api.szamlaiktato.hu/ping",
        json={"status_id": 4001, "status": "Unauthorized"},
        status=200,
    )

    try:
        resp = api.ping(PingRequest())
        print(f"DID NOT RAISE! Response was: {resp}")
    except ApiError as e:
        print("RAISED:", e)

test_client_error()

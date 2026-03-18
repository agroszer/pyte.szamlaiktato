import pytest
import responses
from src.pyte.szamlaiktato.client import OnlineSzamlazoClient, ApiError
from src.pyte.szamlaiktato.api import SzamlaiktatoAPI, PingRequest

@responses.activate
def test_client_call():
    client = OnlineSzamlazoClient("https://api.szamlaiktato.hu", "test_uid", "test_pass", "test_block")
    api = SzamlaiktatoAPI(client)

    responses.add(
        responses.POST,
        "https://api.szamlaiktato.hu/ping",
        json={"status_id": 1000, "status": "OK"},
        status=200
    )

    req = PingRequest(instance_id="123")
    resp = api.ping(req)

    assert resp.status_id == 1000
    assert resp.status == "OK"

@responses.activate
def test_client_error():
    client = OnlineSzamlazoClient("https://api.szamlaiktato.hu", "test_uid", "test_pass", "test_block")
    api = SzamlaiktatoAPI(client)

    responses.add(
        responses.POST,
        "https://api.szamlaiktato.hu/ping",
        json={"status_id": 4001, "status": "Unauthorized"},
        status=200
    )

    with pytest.raises(ApiError) as excinfo:
        api.ping(PingRequest(instance_id="123"))

    assert excinfo.value.status_id == 4001
    assert "Unauthorized" in str(excinfo.value)

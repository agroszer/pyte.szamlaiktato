import pytest
import responses
from pyte.szamlaiktato.client import OnlineSzamlazoClient, ApiError
from pyte.szamlaiktato.api import SzamlaiktatoAPI, PingRequest


@responses.activate
def test_client_call():
    client = OnlineSzamlazoClient(
        "https://api.szamlaiktato.hu",
        "test_uid",
        "test_pass",
        "test_block",
        instance_id="123",
    )
    api = SzamlaiktatoAPI(client)

    responses.add(
        responses.POST,
        "https://api.szamlaiktato.hu/ping",
        json={"status_id": 1000, "status": "OK"},
        status=200,
    )

    req = PingRequest()
    resp = api.ping(req)

    assert resp.status_id == 1000
    assert resp.status == "OK"


@responses.activate
def test_client_error():
    client = OnlineSzamlazoClient(
        "https://api.szamlaiktato.hu",
        "test_uid",
        "test_pass",
        "test_block",
        instance_id="123",
    )
    api = SzamlaiktatoAPI(client)

    responses.add(
        responses.POST,
        "https://api.szamlaiktato.hu/ping",
        json={"status_id": 4001, "status": "Unauthorized"},
        status=200,
    )

    with pytest.raises(ApiError) as excinfo:
        api.ping(PingRequest())

    assert excinfo.value.status_id == 4001
    assert "Unauthorized" in str(excinfo.value)

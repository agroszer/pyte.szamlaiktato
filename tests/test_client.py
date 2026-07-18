import hashlib
import hmac
from unittest.mock import patch

import pytest
import responses

from pyte.szamlaiktato.api import PingRequest, SzamlaiktatoAPI
from pyte.szamlaiktato.client import ApiError, OnlineSzamlazoClient


def test_client_call_password():
    with responses.RequestsMock() as rsps:
        client = OnlineSzamlazoClient(
            "https://api.szamlaiktato.hu",
            "test_uid",
            "test_pass",
            "test_block",
            instance_id="123",
            auth_mode="password",
        )
        assert client.auth_mode == "password"
        api = SzamlaiktatoAPI(client)

        rsps.add(
            responses.POST,
            "https://api.szamlaiktato.hu/ping",
            json={"status_id": 1000, "status": "OK"},
            status=200,
        )

        req = PingRequest()
        resp = api.ping(req)

        assert resp.status_id == 1000
        assert resp.status == "OK"

        import json

        req_body = json.loads(rsps.calls[0].request.body)
        assert req_body["uid"] == "test_uid"
        assert req_body["password"] == "test_pass"
        assert "block" not in req_body
        assert req_body["instance_id"] == "123"


@patch("time.time")
def test_client_call_hmac(mock_time):
    # Set a fixed timestamp
    mock_time.return_value = 1711878000

    with responses.RequestsMock() as rsps:
        client = OnlineSzamlazoClient(
            "https://api.szamlaiktato.hu",
            "test_uid",
            "test_pass",
            "test_block",
            instance_id="123",
        )
        assert client.auth_mode == "hmac"  # Default should be HMAC
        api = SzamlaiktatoAPI(client)

        rsps.add(
            responses.POST,
            "https://api.szamlaiktato.hu/ping",
            json={"status_id": 1000, "status": "OK"},
            status=200,
        )

        req = PingRequest()
        resp = api.ping(req)

        assert resp.status_id == 1000
        assert resp.status == "OK"

        import json

        req_body = json.loads(rsps.calls[0].request.body)
        assert req_body["uid"] == "test_uid"

        # Calculate expected hmac
        expected_ts = 1711878000
        expected_msg = str(expected_ts).encode("ascii")
        expected_key = "test_pass".encode("utf-8")
        expected_sig = hmac.new(expected_key, expected_msg, hashlib.sha256).hexdigest()
        expected_password = f"hmac_{expected_ts}_{expected_sig}"

        assert req_body["password"] == expected_password
        assert "block" not in req_body
        assert req_body["instance_id"] == "123"


def test_client_invalid_auth_mode():
    with pytest.raises(ValueError) as excinfo:
        OnlineSzamlazoClient(
            "https://api.szamlaiktato.hu",
            "test_uid",
            "test_pass",
            "test_block",
            auth_mode="invalid",
        )
    assert "Invalid auth_mode" in str(excinfo.value)


def test_client_error():
    with responses.RequestsMock() as rsps:
        client = OnlineSzamlazoClient(
            "https://api.szamlaiktato.hu",
            "test_uid",
            "test_pass",
            "test_block",
            instance_id="123",
        )
        api = SzamlaiktatoAPI(client)

        rsps.add(
            responses.POST,
            "https://api.szamlaiktato.hu/ping",
            json={"status_id": 4001, "status": "Unauthorized"},
            status=200,
        )

        with pytest.raises(ApiError) as excinfo:
            api.ping(PingRequest())

        assert excinfo.value.status_id == 4001
        assert "Unauthorized" in str(excinfo.value)

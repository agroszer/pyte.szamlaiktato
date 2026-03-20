from typing import Any

import logging
import requests  # type: ignore

LOG = logging.getLogger(__name__)


class ApiError(Exception):
    def __init__(self, action: str, response: dict[str, Any]):
        status_id = response.get("status_id", 0)
        status = response.get("status", "Unknown Error")
        super().__init__(f"API error {status_id}: {status} ({action})")
        self.status_id = status_id
        self.action = action
        self.response = response


class OnlineSzamlazoClient:
    def __init__(
        self,
        api_url: str,
        uid: str,
        password: str,
        block: str,
        instance_id: str | None = None,
    ):
        self.api_url = api_url.rstrip("/")
        self.uid = uid
        self.password = password
        self.block = block
        self.instance_id = instance_id

    def _call(
        self,
        method: str,
        params: dict[str, Any] | None = None,
        skip_block: bool = False,
        requires_instance_id: bool = True,
    ) -> dict[str, Any]:
        url = f"{self.api_url}/{method}"

        body = {
            "uid": self.uid,
            "password": self.password,
        }

        if params:
            # We want to exclude None values if dataclasses produce them
            filtered_params = {k: v for k, v in params.items() if v is not None}
            body.update(filtered_params)

        if not skip_block and "block" not in body:
            body["block"] = self.block

        if (
            requires_instance_id
            and self.instance_id is not None
            and "instance_id" not in body
        ):
            body["instance_id"] = self.instance_id

        bodydupe = {}
        bodydupe.update(body)
        bodydupe["password"] = "***"
        LOG.info("Request URL:\n%s\npayload:\n%r", url, bodydupe)

        response = requests.post(
            url, json=body, headers={"Content-Type": "application/json"}
        )
        if response.status_code >= 400:
            LOG.error("Response URL:\n%s\n%s", url, response)
        response.raise_for_status()

        data = response.json()
        LOG.info("Response URL:\n%s, data:\n%r", url, data)

        status_id = data.get("status_id")
        if status_id is not None and int(status_id) >= 4000:
            raise ApiError(method, data)

        return data

from __future__ import annotations

from ..models import (
    BaseHost,
    BulkHostsActionResponse,
    BulkHostSelection,
    CreateHost,
    RemoveHostsResponse,
)


class HostMixin:
    async def get_host(self, host_id: int, token: str | None = None) -> BaseHost:
        url = f"/api/host/{host_id}"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, BaseHost)

    async def modify_host(self, host_id: int, host: CreateHost, token: str | None = None) -> BaseHost:
        url = f"/api/host/{host_id}"
        params = None
        headers = None
        payload = self._validate_payload(host, CreateHost)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BaseHost)

    async def remove_host(self, host_id: int, token: str | None = None) -> None:
        url = f"/api/host/{host_id}"
        params = None
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def get_hosts(
        self, token: str | None = None, ids: list[int] | None = None, offset: int | None = 0, limit: int | None = 0
    ) -> list[BaseHost]:
        url = "/api/hosts"
        params = {"ids": ids, "offset": offset, "limit": limit}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, list[BaseHost])

    async def modify_hosts(self, hosts: list[CreateHost], token: str | None = None) -> list[BaseHost]:
        url = "/api/hosts"
        params = None
        headers = None
        payload = self._validate_payload(hosts, list[CreateHost])
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, list[BaseHost])

    async def create_host(self, host: CreateHost, token: str | None = None) -> BaseHost:
        url = "/api/host/"
        params = None
        headers = None
        payload = self._validate_payload(host, CreateHost)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BaseHost)

    async def bulk_delete_hosts(self, bulk: BulkHostSelection, token: str | None = None) -> RemoveHostsResponse:
        url = "/api/hosts/bulk/delete"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkHostSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, RemoveHostsResponse)

    async def bulk_disable_hosts(self, bulk: BulkHostSelection, token: str | None = None) -> BulkHostsActionResponse:
        url = "/api/hosts/bulk/disable"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkHostSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkHostsActionResponse)

    async def bulk_enable_hosts(self, bulk: BulkHostSelection, token: str | None = None) -> BulkHostsActionResponse:
        url = "/api/hosts/bulk/enable"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkHostSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkHostsActionResponse)

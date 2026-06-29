from __future__ import annotations

from ..models import (
    BulkCoreSelection,
    CoreCreate,
    CoreResponse,
    CoreResponseList,
    CoresSimpleResponse,
    RemoveCoresResponse,
)


class CoreMixin:
    async def create_core_config(self, core: CoreCreate, token: str | None = None) -> CoreResponse:
        url = "/api/core"
        params = None
        headers = None
        payload = self._validate_payload(core, CoreCreate)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, CoreResponse)

    async def get_core_config(self, core_id: int, token: str | None = None) -> CoreResponse:
        url = f"/api/core/{core_id}"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, CoreResponse)

    async def modify_core_config(
        self, core_id: int, core: CoreCreate, restart_nodes: bool, token: str | None = None
    ) -> CoreResponse:
        url = f"/api/core/{core_id}"
        params = {"restart_nodes": restart_nodes}
        headers = None
        payload = self._validate_payload(core, CoreCreate)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, CoreResponse)

    async def delete_core_config(
        self, core_id: int, token: str | None = None, restart_nodes: bool | None = False
    ) -> None:
        url = f"/api/core/{core_id}"
        params = {"restart_nodes": restart_nodes}
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def get_all_cores(
        self,
        token: str | None = None,
        ids: list[int] | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> CoreResponseList:
        url = "/api/cores"
        params = {"ids": ids, "offset": offset, "limit": limit}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, CoreResponseList)

    async def get_cores_simple(
        self,
        token: str | None = None,
        ids: list[int] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        search: str | None = None,
        sort: str | None = None,
        all: bool | None = False,
    ) -> CoresSimpleResponse:
        url = "/api/cores/simple"
        params = {"ids": ids, "offset": offset, "limit": limit, "search": search, "sort": sort, "all": all}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, CoresSimpleResponse)

    async def restart_core(self, core_id: int, token: str | None = None) -> None:
        url = f"/api/core/{core_id}/restart"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def bulk_delete_cores(self, bulk: BulkCoreSelection, token: str | None = None) -> RemoveCoresResponse:
        url = "/api/cores/bulk/delete"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkCoreSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, RemoveCoresResponse)

from __future__ import annotations

# ruff: noqa: F401, F403
from ._imports import *


class CoreMixin:
    async def create_core_config(self, core: CoreCreate, token: str) -> CoreResponse:
        url = '/api/core'
        params = None
        headers = None
        payload = self._validate_payload(core, CoreCreate)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, CoreResponse)

    async def get_core_config(self, core_id: int, token: str) -> CoreResponse:
        url = '/api/core/{core_id}'.format(core_id=core_id)
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, CoreResponse)

    async def modify_core_config(self, core_id: int, core: CoreCreate, restart_nodes: bool, token: str) -> CoreResponse:
        url = '/api/core/{core_id}'.format(core_id=core_id)
        params = {'restart_nodes': restart_nodes}
        headers = None
        payload = self._validate_payload(core, CoreCreate)
        response = await self._request('PUT', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, CoreResponse)

    async def delete_core_config(self, core_id: int, token: str, restart_nodes: Optional[bool] = False) -> None:
        url = '/api/core/{core_id}'.format(core_id=core_id)
        params = {'restart_nodes': restart_nodes}
        headers = None
        response = await self._request('DELETE', url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def get_all_cores(self, token: str, ids: Optional[List[int]] = None, offset: Optional[int] = None, limit: Optional[int] = None) -> CoreResponseList:
        url = '/api/cores'
        params = {'ids': ids, 'offset': offset, 'limit': limit}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, CoreResponseList)

    async def get_cores_simple(self, token: str, ids: Optional[List[int]] = None, offset: Optional[int] = None, limit: Optional[int] = None, search: Optional[str] = None, sort: Optional[str] = None, all: Optional[bool] = False) -> CoresSimpleResponse:
        url = '/api/cores/simple'
        params = {'ids': ids, 'offset': offset, 'limit': limit, 'search': search, 'sort': sort, 'all': all}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, CoresSimpleResponse)

    async def restart_core(self, core_id: int, token: str) -> None:
        url = '/api/core/{core_id}/restart'.format(core_id=core_id)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def bulk_delete_cores(self, bulk: BulkCoreSelection, token: str) -> RemoveCoresResponse:
        url = '/api/cores/bulk/delete'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkCoreSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, RemoveCoresResponse)

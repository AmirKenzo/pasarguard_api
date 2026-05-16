from __future__ import annotations

# ruff: noqa: F401, F403
from ._imports import *


class ClientTemplateMixin:
    async def create_client_template(self, template: ClientTemplateCreate, token: str) -> ClientTemplateResponse:
        url = '/api/client_template'
        params = None
        headers = None
        payload = self._validate_payload(template, ClientTemplateCreate)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, ClientTemplateResponse)

    async def get_client_template(self, template_id: int, token: str) -> ClientTemplateResponse:
        url = '/api/client_template/{template_id}'.format(template_id=template_id)
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, ClientTemplateResponse)

    async def modify_client_template(self, template_id: int, template: ClientTemplateModify, token: str) -> ClientTemplateResponse:
        url = '/api/client_template/{template_id}'.format(template_id=template_id)
        params = None
        headers = None
        payload = self._validate_payload(template, ClientTemplateModify)
        response = await self._request('PUT', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, ClientTemplateResponse)

    async def remove_client_template(self, template_id: int, token: str) -> None:
        url = '/api/client_template/{template_id}'.format(template_id=template_id)
        params = None
        headers = None
        response = await self._request('DELETE', url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def get_client_templates(self, token: str, ids: Optional[List[int]] = None, template_type: Optional[ClientTemplateType] = None, offset: Optional[int] = None, limit: Optional[int] = None) -> ClientTemplateResponseList:
        url = '/api/client_templates'
        params = {'ids': ids, 'template_type': template_type, 'offset': offset, 'limit': limit}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, ClientTemplateResponseList)

    async def get_client_templates_simple(self, token: str, ids: Optional[List[int]] = None, template_type: Optional[ClientTemplateType] = None, offset: Optional[int] = None, limit: Optional[int] = None, search: Optional[str] = None, sort: Optional[str] = None, all: Optional[bool] = False) -> ClientTemplatesSimpleResponse:
        url = '/api/client_templates/simple'
        params = {'ids': ids, 'template_type': template_type, 'offset': offset, 'limit': limit, 'search': search, 'sort': sort, 'all': all}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, ClientTemplatesSimpleResponse)

    async def bulk_delete_client_templates(self, bulk: BulkClientTemplateSelection, token: str) -> RemoveClientTemplatesResponse:
        url = '/api/client_templates/bulk/delete'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkClientTemplateSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, RemoveClientTemplatesResponse)

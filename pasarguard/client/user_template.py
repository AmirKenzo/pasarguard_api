from __future__ import annotations

from ._imports import (
    BulkUserTemplateSelection,
    BulkUserTemplatesActionResponse,
    List,
    Optional,
    RemoveUserTemplatesResponse,
    UserTemplateCreate,
    UserTemplateModify,
    UserTemplateResponse,
    UserTemplatesSimpleResponse,
)


class UserTemplateMixin:
    async def create_user_template(self, template: UserTemplateCreate, token: str) -> UserTemplateResponse:
        url = '/api/user_template'
        params = None
        headers = None
        payload = self._validate_payload(template, UserTemplateCreate)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserTemplateResponse)

    async def get_user_template(self, template_id: int, token: str) -> UserTemplateResponse:
        url = '/api/user_template/{template_id}'.format(template_id=template_id)
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserTemplateResponse)

    async def modify_user_template(self, template_id: int, template: UserTemplateModify, token: str) -> UserTemplateResponse:
        url = '/api/user_template/{template_id}'.format(template_id=template_id)
        params = None
        headers = None
        payload = self._validate_payload(template, UserTemplateModify)
        response = await self._request('PUT', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserTemplateResponse)

    async def remove_user_template(self, template_id: int, token: str) -> None:
        url = '/api/user_template/{template_id}'.format(template_id=template_id)
        params = None
        headers = None
        response = await self._request('DELETE', url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def get_user_templates(self, token: str, ids: Optional[List[int]] = None, offset: Optional[int] = None, limit: Optional[int] = None) -> List[UserTemplateResponse]:
        url = '/api/user_templates'
        params = {'ids': ids, 'offset': offset, 'limit': limit}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, List[UserTemplateResponse])

    async def get_user_templates_simple(self, token: str, ids: Optional[List[int]] = None, offset: Optional[int] = None, limit: Optional[int] = None, search: Optional[str] = None, sort: Optional[str] = None, all: Optional[bool] = False) -> UserTemplatesSimpleResponse:
        url = '/api/user_templates/simple'
        params = {'ids': ids, 'offset': offset, 'limit': limit, 'search': search, 'sort': sort, 'all': all}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserTemplatesSimpleResponse)

    async def bulk_delete_user_templates(self, bulk: BulkUserTemplateSelection, token: str) -> RemoveUserTemplatesResponse:
        url = '/api/user_templates/bulk/delete'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUserTemplateSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, RemoveUserTemplatesResponse)

    async def bulk_disable_user_templates(self, bulk: BulkUserTemplateSelection, token: str) -> BulkUserTemplatesActionResponse:
        url = '/api/user_templates/bulk/disable'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUserTemplateSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUserTemplatesActionResponse)

    async def bulk_enable_user_templates(self, bulk: BulkUserTemplateSelection, token: str) -> BulkUserTemplatesActionResponse:
        url = '/api/user_templates/bulk/enable'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUserTemplateSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUserTemplatesActionResponse)

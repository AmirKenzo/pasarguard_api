from __future__ import annotations

from ..models import (
    BulkUserTemplatesActionResponse,
    BulkUserTemplateSelection,
    RemoveUserTemplatesResponse,
    UserTemplateCreate,
    UserTemplateModify,
    UserTemplateResponse,
    UserTemplatesSimpleResponse,
)


class UserTemplateMixin:
    async def create_user_template(
        self, template: UserTemplateCreate, token: str | None = None
    ) -> UserTemplateResponse:
        url = "/api/user_template"
        params = None
        headers = None
        payload = self._validate_payload(template, UserTemplateCreate)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserTemplateResponse)

    async def get_user_template(self, template_id: int, token: str | None = None) -> UserTemplateResponse:
        url = f"/api/user_template/{template_id}"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserTemplateResponse)

    async def modify_user_template(
        self, template_id: int, template: UserTemplateModify, token: str | None = None
    ) -> UserTemplateResponse:
        url = f"/api/user_template/{template_id}"
        params = None
        headers = None
        payload = self._validate_payload(template, UserTemplateModify)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserTemplateResponse)

    async def remove_user_template(self, template_id: int, token: str | None = None) -> None:
        url = f"/api/user_template/{template_id}"
        params = None
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def get_user_templates(
        self,
        token: str | None = None,
        ids: list[int] | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> list[UserTemplateResponse]:
        url = "/api/user_templates"
        params = {"ids": ids, "offset": offset, "limit": limit}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, list[UserTemplateResponse])

    async def get_user_templates_simple(
        self,
        token: str | None = None,
        ids: list[int] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        search: str | None = None,
        sort: str | None = None,
        all: bool | None = False,
    ) -> UserTemplatesSimpleResponse:
        url = "/api/user_templates/simple"
        params = {"ids": ids, "offset": offset, "limit": limit, "search": search, "sort": sort, "all": all}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserTemplatesSimpleResponse)

    async def bulk_delete_user_templates(
        self, bulk: BulkUserTemplateSelection, token: str | None = None
    ) -> RemoveUserTemplatesResponse:
        url = "/api/user_templates/bulk/delete"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUserTemplateSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, RemoveUserTemplatesResponse)

    async def bulk_disable_user_templates(
        self, bulk: BulkUserTemplateSelection, token: str | None = None
    ) -> BulkUserTemplatesActionResponse:
        url = "/api/user_templates/bulk/disable"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUserTemplateSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUserTemplatesActionResponse)

    async def bulk_enable_user_templates(
        self, bulk: BulkUserTemplateSelection, token: str | None = None
    ) -> BulkUserTemplatesActionResponse:
        url = "/api/user_templates/bulk/enable"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUserTemplateSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUserTemplatesActionResponse)

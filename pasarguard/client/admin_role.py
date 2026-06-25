from __future__ import annotations

from ..models import (
    AdminRoleCreate,
    AdminRoleModify,
    AdminRoleResponse,
    AdminRolesResponse,
    AdminRolesSimpleResponse,
)


class AdminRoleMixin:
    async def create_role(self, role: AdminRoleCreate, token: str) -> AdminRoleResponse:
        url = "/api/admin-role"
        params = None
        headers = None
        payload = self._validate_payload(role, AdminRoleCreate)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, AdminRoleResponse)

    async def get_role(self, role_id: int, token: str) -> AdminRoleResponse:
        url = f"/api/admin-role/{role_id}"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, AdminRoleResponse)

    async def modify_role(self, role_id: int, role: AdminRoleModify, token: str) -> AdminRoleResponse:
        url = f"/api/admin-role/{role_id}"
        params = None
        headers = None
        payload = self._validate_payload(role, AdminRoleModify)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, AdminRoleResponse)

    async def delete_role(self, role_id: int, token: str) -> None:
        url = f"/api/admin-role/{role_id}"
        params = None
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def get_roles(
        self,
        token: str,
        search: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        sort: str | None = None,
    ) -> AdminRolesResponse:
        url = "/api/admin-roles"
        params = {"search": search, "offset": offset, "limit": limit, "sort": sort}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, AdminRolesResponse)

    async def get_roles_simple(self, token: str) -> AdminRolesSimpleResponse:
        url = "/api/admin-roles/simple"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, AdminRolesSimpleResponse)

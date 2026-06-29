from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
)

from ..enums import Period
from ..models import (
    AdminCreate,
    AdminDetails,
    AdminModify,
    AdminsResponse,
    AdminsSimpleResponse,
    BulkAdminsActionResponse,
    BulkAdminSelection,
    RemoveAdminsResponse,
    UserUsageStatsList,
)


class AdminMixin:
    async def admin_mini_app_token(self, x_telegram_authorization: str = ...) -> Any:
        url = "/api/admin/miniapp/token"
        params = None
        headers = {"x-telegram-authorization": x_telegram_authorization}
        response = await self._request("POST", url, authenticated=False, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def get_current_admin(self, token: str | None = None) -> AdminDetails:
        url = "/api/admin"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def create_admin(self, admin: AdminCreate, token: str | None = None) -> AdminDetails:
        url = "/api/admin"
        params = None
        headers = None
        payload = self._validate_payload(admin, AdminCreate)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def modify_admin(self, username: str, admin: AdminModify, token: str | None = None) -> AdminDetails:
        url = f"/api/admin/{username}"
        params = None
        headers = None
        payload = self._validate_payload(admin, AdminModify)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def remove_admin(self, username: str, token: str | None = None) -> None:
        url = f"/api/admin/{username}"
        params = None
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def modify_admin_by_username(
        self, username: str, admin: AdminModify, token: str | None = None
    ) -> AdminDetails:
        url = f"/api/admin/by-username/{username}"
        params = None
        headers = None
        payload = self._validate_payload(admin, AdminModify)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def remove_admin_by_username(self, username: str, token: str | None = None) -> None:
        url = f"/api/admin/by-username/{username}"
        params = None
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def modify_admin_by_id(self, admin_id: int, admin: AdminModify, token: str | None = None) -> AdminDetails:
        url = f"/api/admin/by-id/{admin_id}"
        params = None
        headers = None
        payload = self._validate_payload(admin, AdminModify)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def remove_admin_by_id(self, admin_id: int, token: str | None = None) -> None:
        url = f"/api/admin/by-id/{admin_id}"
        params = None
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def get_admins(
        self,
        token: str | None = None,
        ids: list[int] | None = None,
        usernames: list[str] | None = None,
        username: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        sort: str | None = None,
    ) -> AdminsResponse:
        url = "/api/admins"
        params = {
            "ids": ids,
            "usernames": usernames,
            "username": username,
            "offset": offset,
            "limit": limit,
            "sort": sort,
        }
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, AdminsResponse)

    async def get_admins_simple(
        self,
        token: str | None = None,
        ids: list[int] | None = None,
        usernames: list[str] | None = None,
        search: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        sort: str | None = None,
        all: bool | None = False,
    ) -> AdminsSimpleResponse:
        url = "/api/admins/simple"
        params = {
            "ids": ids,
            "usernames": usernames,
            "search": search,
            "offset": offset,
            "limit": limit,
            "sort": sort,
            "all": all,
        }
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, AdminsSimpleResponse)

    async def get_admin_usage(
        self,
        username: str,
        token: str | None = None,
        period: Period | None = "hour",
        node_id: int | None = None,
        group_by_node: bool | None = False,
        start: datetime | None = None,
        end: datetime | None = None,
    ) -> UserUsageStatsList:
        url = f"/api/admin/{username}/usage"
        params = {"period": period, "node_id": node_id, "group_by_node": group_by_node, "start": start, "end": end}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserUsageStatsList)

    async def get_admin_usage_by_username(
        self,
        username: str,
        token: str | None = None,
        period: Period | None = "hour",
        node_id: int | None = None,
        group_by_node: bool | None = False,
        start: datetime | None = None,
        end: datetime | None = None,
    ) -> UserUsageStatsList:
        url = f"/api/admin/by-username/{username}/usage"
        params = {"period": period, "node_id": node_id, "group_by_node": group_by_node, "start": start, "end": end}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserUsageStatsList)

    async def get_admin_usage_by_id(
        self,
        admin_id: int,
        token: str | None = None,
        period: Period | None = "hour",
        node_id: int | None = None,
        group_by_node: bool | None = False,
        start: datetime | None = None,
        end: datetime | None = None,
    ) -> UserUsageStatsList:
        url = f"/api/admin/by-id/{admin_id}/usage"
        params = {"period": period, "node_id": node_id, "group_by_node": group_by_node, "start": start, "end": end}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserUsageStatsList)

    async def disable_all_active_users(self, username: str, token: str | None = None) -> Any:
        url = f"/api/admin/{username}/users/disable"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def disable_all_active_users_by_username(self, username: str, token: str | None = None) -> Any:
        url = f"/api/admin/by-username/{username}/users/disable"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def disable_all_active_users_by_id(self, admin_id: int, token: str | None = None) -> Any:
        url = f"/api/admin/by-id/{admin_id}/users/disable"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def activate_all_disabled_users(self, username: str, token: str | None = None) -> Any:
        url = f"/api/admin/{username}/users/activate"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def activate_all_disabled_users_by_username(self, username: str, token: str | None = None) -> Any:
        url = f"/api/admin/by-username/{username}/users/activate"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def activate_all_disabled_users_by_id(self, admin_id: int, token: str | None = None) -> Any:
        url = f"/api/admin/by-id/{admin_id}/users/activate"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def remove_all_users(self, username: str, token: str | None = None) -> Any:
        url = f"/api/admin/{username}/users"
        params = None
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def remove_all_users_by_username(self, username: str, token: str | None = None) -> Any:
        url = f"/api/admin/by-username/{username}/users"
        params = None
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def remove_all_users_by_id(self, admin_id: int, token: str | None = None) -> Any:
        url = f"/api/admin/by-id/{admin_id}/users"
        params = None
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def reset_admin_usage(self, username: str, token: str | None = None) -> AdminDetails:
        url = f"/api/admin/{username}/reset"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def reset_admin_usage_by_username(self, username: str, token: str | None = None) -> AdminDetails:
        url = f"/api/admin/by-username/{username}/reset"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def reset_admin_usage_by_id(self, admin_id: int, token: str | None = None) -> AdminDetails:
        url = f"/api/admin/by-id/{admin_id}/reset"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def bulk_delete_admins(self, bulk: BulkAdminSelection, token: str | None = None) -> RemoveAdminsResponse:
        url = "/api/admins/bulk/delete"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkAdminSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, RemoveAdminsResponse)

    async def bulk_reset_admins_usage(
        self, bulk: BulkAdminSelection, token: str | None = None
    ) -> BulkAdminsActionResponse:
        url = "/api/admins/bulk/reset"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkAdminSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkAdminsActionResponse)

    async def bulk_disable_admins(self, bulk: BulkAdminSelection, token: str | None = None) -> BulkAdminsActionResponse:
        url = "/api/admins/bulk/disable"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkAdminSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkAdminsActionResponse)

    async def bulk_enable_admins(self, bulk: BulkAdminSelection, token: str | None = None) -> BulkAdminsActionResponse:
        url = "/api/admins/bulk/enable"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkAdminSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkAdminsActionResponse)

    async def bulk_disable_all_active_users(
        self, bulk: BulkAdminSelection, token: str | None = None
    ) -> BulkAdminsActionResponse:
        url = "/api/admins/bulk/users/disable"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkAdminSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkAdminsActionResponse)

    async def bulk_activate_all_disabled_users(
        self, bulk: BulkAdminSelection, token: str | None = None
    ) -> BulkAdminsActionResponse:
        url = "/api/admins/bulk/users/activate"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkAdminSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkAdminsActionResponse)

    async def bulk_remove_all_users(
        self, bulk: BulkAdminSelection, token: str | None = None
    ) -> BulkAdminsActionResponse:
        url = "/api/admins/bulk/users"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkAdminSelection)
        response = await self._request("DELETE", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkAdminsActionResponse)

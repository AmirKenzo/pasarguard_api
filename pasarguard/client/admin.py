from __future__ import annotations

from ._imports import (
    AdminCreate,
    AdminDetails,
    AdminModify,
    AdminsResponse,
    AdminsSimpleResponse,
    Any,
    BulkAdminSelection,
    BulkAdminsActionResponse,
    List,
    Optional,
    Period,
    RemoveAdminsResponse,
    UserUsageStatsList,
    datetime,
)


class AdminMixin:
    async def admin_mini_app_token(self, x_telegram_authorization: str = ...) -> Any:
        url = '/api/admin/miniapp/token'
        params = None
        headers = {'x-telegram-authorization': x_telegram_authorization}
        response = await self._request('POST', url, token=None, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def get_current_admin(self, token: str) -> AdminDetails:
        url = '/api/admin'
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def create_admin(self, admin: AdminCreate, token: str) -> AdminDetails:
        url = '/api/admin'
        params = None
        headers = None
        payload = self._validate_payload(admin, AdminCreate)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def modify_admin(self, username: str, admin: AdminModify, token: str) -> AdminDetails:
        url = '/api/admin/{username}'.format(username=username)
        params = None
        headers = None
        payload = self._validate_payload(admin, AdminModify)
        response = await self._request('PUT', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def remove_admin(self, username: str, token: str) -> None:
        url = '/api/admin/{username}'.format(username=username)
        params = None
        headers = None
        response = await self._request('DELETE', url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def modify_admin_by_username(self, username: str, admin: AdminModify, token: str) -> AdminDetails:
        url = '/api/admin/by-username/{username}'.format(username=username)
        params = None
        headers = None
        payload = self._validate_payload(admin, AdminModify)
        response = await self._request('PUT', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def remove_admin_by_username(self, username: str, token: str) -> None:
        url = '/api/admin/by-username/{username}'.format(username=username)
        params = None
        headers = None
        response = await self._request('DELETE', url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def modify_admin_by_id(self, admin_id: int, admin: AdminModify, token: str) -> AdminDetails:
        url = '/api/admin/by-id/{admin_id}'.format(admin_id=admin_id)
        params = None
        headers = None
        payload = self._validate_payload(admin, AdminModify)
        response = await self._request('PUT', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def remove_admin_by_id(self, admin_id: int, token: str) -> None:
        url = '/api/admin/by-id/{admin_id}'.format(admin_id=admin_id)
        params = None
        headers = None
        response = await self._request('DELETE', url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def get_admins(self, token: str, ids: Optional[List[int]] = None, usernames: Optional[List[str]] = None, username: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None, sort: Optional[str] = None) -> AdminsResponse:
        url = '/api/admins'
        params = {'ids': ids, 'usernames': usernames, 'username': username, 'offset': offset, 'limit': limit, 'sort': sort}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, AdminsResponse)

    async def get_admins_simple(self, token: str, ids: Optional[List[int]] = None, usernames: Optional[List[str]] = None, search: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None, sort: Optional[str] = None, all: Optional[bool] = False) -> AdminsSimpleResponse:
        url = '/api/admins/simple'
        params = {'ids': ids, 'usernames': usernames, 'search': search, 'offset': offset, 'limit': limit, 'sort': sort, 'all': all}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, AdminsSimpleResponse)

    async def get_admin_usage(self, username: str, token: str, period: Optional[Period] = 'hour', node_id: Optional[int] = None, group_by_node: Optional[bool] = False, start: Optional[datetime] = None, end: Optional[datetime] = None) -> UserUsageStatsList:
        url = '/api/admin/{username}/usage'.format(username=username)
        params = {'period': period, 'node_id': node_id, 'group_by_node': group_by_node, 'start': start, 'end': end}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserUsageStatsList)

    async def get_admin_usage_by_username(self, username: str, token: str, period: Optional[Period] = 'hour', node_id: Optional[int] = None, group_by_node: Optional[bool] = False, start: Optional[datetime] = None, end: Optional[datetime] = None) -> UserUsageStatsList:
        url = '/api/admin/by-username/{username}/usage'.format(username=username)
        params = {'period': period, 'node_id': node_id, 'group_by_node': group_by_node, 'start': start, 'end': end}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserUsageStatsList)

    async def get_admin_usage_by_id(self, admin_id: int, token: str, period: Optional[Period] = 'hour', node_id: Optional[int] = None, group_by_node: Optional[bool] = False, start: Optional[datetime] = None, end: Optional[datetime] = None) -> UserUsageStatsList:
        url = '/api/admin/by-id/{admin_id}/usage'.format(admin_id=admin_id)
        params = {'period': period, 'node_id': node_id, 'group_by_node': group_by_node, 'start': start, 'end': end}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserUsageStatsList)

    async def disable_all_active_users(self, username: str, token: str) -> Any:
        url = '/api/admin/{username}/users/disable'.format(username=username)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def disable_all_active_users_by_username(self, username: str, token: str) -> Any:
        url = '/api/admin/by-username/{username}/users/disable'.format(username=username)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def disable_all_active_users_by_id(self, admin_id: int, token: str) -> Any:
        url = '/api/admin/by-id/{admin_id}/users/disable'.format(admin_id=admin_id)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def activate_all_disabled_users(self, username: str, token: str) -> Any:
        url = '/api/admin/{username}/users/activate'.format(username=username)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def activate_all_disabled_users_by_username(self, username: str, token: str) -> Any:
        url = '/api/admin/by-username/{username}/users/activate'.format(username=username)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def activate_all_disabled_users_by_id(self, admin_id: int, token: str) -> Any:
        url = '/api/admin/by-id/{admin_id}/users/activate'.format(admin_id=admin_id)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def remove_all_users(self, username: str, token: str) -> Any:
        url = '/api/admin/{username}/users'.format(username=username)
        params = None
        headers = None
        response = await self._request('DELETE', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def remove_all_users_by_username(self, username: str, token: str) -> Any:
        url = '/api/admin/by-username/{username}/users'.format(username=username)
        params = None
        headers = None
        response = await self._request('DELETE', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def remove_all_users_by_id(self, admin_id: int, token: str) -> Any:
        url = '/api/admin/by-id/{admin_id}/users'.format(admin_id=admin_id)
        params = None
        headers = None
        response = await self._request('DELETE', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def reset_admin_usage(self, username: str, token: str) -> AdminDetails:
        url = '/api/admin/{username}/reset'.format(username=username)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def reset_admin_usage_by_username(self, username: str, token: str) -> AdminDetails:
        url = '/api/admin/by-username/{username}/reset'.format(username=username)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def reset_admin_usage_by_id(self, admin_id: int, token: str) -> AdminDetails:
        url = '/api/admin/by-id/{admin_id}/reset'.format(admin_id=admin_id)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def bulk_delete_admins(self, bulk: BulkAdminSelection, token: str) -> RemoveAdminsResponse:
        url = '/api/admins/bulk/delete'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkAdminSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, RemoveAdminsResponse)

    async def bulk_reset_admins_usage(self, bulk: BulkAdminSelection, token: str) -> BulkAdminsActionResponse:
        url = '/api/admins/bulk/reset'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkAdminSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkAdminsActionResponse)

    async def bulk_disable_admins(self, bulk: BulkAdminSelection, token: str) -> BulkAdminsActionResponse:
        url = '/api/admins/bulk/disable'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkAdminSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkAdminsActionResponse)

    async def bulk_enable_admins(self, bulk: BulkAdminSelection, token: str) -> BulkAdminsActionResponse:
        url = '/api/admins/bulk/enable'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkAdminSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkAdminsActionResponse)

    async def bulk_disable_all_active_users(self, bulk: BulkAdminSelection, token: str) -> BulkAdminsActionResponse:
        url = '/api/admins/bulk/users/disable'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkAdminSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkAdminsActionResponse)

    async def bulk_activate_all_disabled_users(self, bulk: BulkAdminSelection, token: str) -> BulkAdminsActionResponse:
        url = '/api/admins/bulk/users/activate'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkAdminSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkAdminsActionResponse)

    async def bulk_remove_all_users(self, bulk: BulkAdminSelection, token: str) -> BulkAdminsActionResponse:
        url = '/api/admins/bulk/users'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkAdminSelection)
        response = await self._request('DELETE', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkAdminsActionResponse)

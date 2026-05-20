from __future__ import annotations

from ._imports import (
    Any,
    BulkUser,
    BulkUsersActionResponse,
    BulkUsersApplyTemplate,
    BulkUsersCreateResponse,
    BulkUsersFromTemplate,
    BulkUsersProxy,
    BulkUsersSelection,
    BulkUsersSetOwner,
    BulkWireGuardPeerIPs,
    ConfigFormat,
    CreateUserFromTemplate,
    DataLimitResetStrategy,
    List,
    Literal,
    ModifyUserByTemplate,
    Optional,
    Period,
    RemoveUsersResponse,
    Union,
    UserCountMetric,
    UserCountMetricStatsList,
    UserCreate,
    UserModify,
    UserResponse,
    UserStatus,
    UserSubscriptionUpdateChart,
    UserSubscriptionUpdateList,
    UserUsageStatsList,
    UsersResponse,
    UsersSimpleResponse,
    WireGuardPeerIPsReallocateResponse,
    datetime,
)

ExpiredUsersTarget = Literal["expired", "limited"]


class UserMixin:
    async def create_user(self, user: UserCreate, token: str) -> UserResponse:
        url = '/api/user'
        params = None
        headers = None
        payload = self._validate_payload(user, UserCreate)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def modify_user(self, username: str, user: UserModify, token: str) -> UserResponse:
        url = '/api/user/{username}'.format(username=username)
        params = None
        headers = None
        payload = self._validate_payload(user, UserModify)
        response = await self._request('PUT', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def remove_user(self, username: str, token: str) -> None:
        url = '/api/user/{username}'.format(username=username)
        params = None
        headers = None
        response = await self._request('DELETE', url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def get_user(self, username: str, token: str) -> UserResponse:
        url = '/api/user/{username}'.format(username=username)
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def modify_user_by_username(self, username: str, user: UserModify, token: str) -> UserResponse:
        url = '/api/user/by-username/{username}'.format(username=username)
        params = None
        headers = None
        payload = self._validate_payload(user, UserModify)
        response = await self._request('PUT', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def remove_user_by_username(self, username: str, token: str) -> None:
        url = '/api/user/by-username/{username}'.format(username=username)
        params = None
        headers = None
        response = await self._request('DELETE', url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def get_user_by_username(self, username: str, token: str) -> UserResponse:
        url = '/api/user/by-username/{username}'.format(username=username)
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def modify_user_by_id(self, user_id: int, user: UserModify, token: str) -> UserResponse:
        url = '/api/user/by-id/{user_id}'.format(user_id=user_id)
        params = None
        headers = None
        payload = self._validate_payload(user, UserModify)
        response = await self._request('PUT', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def remove_user_by_id(self, user_id: int, token: str) -> None:
        url = '/api/user/by-id/{user_id}'.format(user_id=user_id)
        params = None
        headers = None
        response = await self._request('DELETE', url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def get_user_by_id(self, user_id: int, token: str) -> UserResponse:
        url = '/api/user/by-id/{user_id}'.format(user_id=user_id)
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def reset_user_data_usage(self, username: str, token: str) -> UserResponse:
        url = '/api/user/{username}/reset'.format(username=username)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def reset_user_data_usage_by_username(self, username: str, token: str) -> UserResponse:
        url = '/api/user/by-username/{username}/reset'.format(username=username)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def reset_user_data_usage_by_id(self, user_id: int, token: str) -> UserResponse:
        url = '/api/user/by-id/{user_id}/reset'.format(user_id=user_id)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def revoke_user_subscription(self, username: str, token: str) -> UserResponse:
        url = '/api/user/{username}/revoke_sub'.format(username=username)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def revoke_user_subscription_by_username(self, username: str, token: str) -> UserResponse:
        url = '/api/user/by-username/{username}/revoke_sub'.format(username=username)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def revoke_user_subscription_by_id(self, user_id: int, token: str) -> UserResponse:
        url = '/api/user/by-id/{user_id}/revoke_sub'.format(user_id=user_id)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def reset_users_data_usage(self, token: str) -> Any:
        url = '/api/users/reset'
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def get_users_sub_update_chart(self, token: str, user_id: Optional[int] = None, username: Optional[str] = None, admin_id: Optional[int] = None) -> UserSubscriptionUpdateChart:
        url = '/api/users/sub_update/chart'
        params = {'user_id': user_id, 'username': username, 'admin_id': admin_id}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserSubscriptionUpdateChart)

    async def set_owner(self, username: str, admin_username: str, token: str) -> UserResponse:
        url = '/api/user/{username}/set_owner'.format(username=username)
        params = {'admin_username': admin_username}
        headers = None
        response = await self._request('PUT', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def set_owner_by_username(self, username: str, admin_username: str, token: str) -> UserResponse:
        url = '/api/user/by-username/{username}/set_owner'.format(username=username)
        params = {'admin_username': admin_username}
        headers = None
        response = await self._request('PUT', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def set_owner_by_id(self, user_id: int, admin_username: str, token: str) -> UserResponse:
        url = '/api/user/by-id/{user_id}/set_owner'.format(user_id=user_id)
        params = {'admin_username': admin_username}
        headers = None
        response = await self._request('PUT', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def active_next_plan(self, username: str, token: str) -> UserResponse:
        url = '/api/user/{username}/active_next'.format(username=username)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def active_next_plan_by_username(self, username: str, token: str) -> UserResponse:
        url = '/api/user/by-username/{username}/active_next'.format(username=username)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def active_next_plan_by_id(self, user_id: int, token: str) -> UserResponse:
        url = '/api/user/by-id/{user_id}/active_next'.format(user_id=user_id)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def get_user_subscription_by_id(self, user_id: int, client_type: ConfigFormat, token: str) -> Any:
        url = '/api/user/{user_id}/subscription/{client_type}'.format(user_id=user_id, client_type=client_type)
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def get_user_sub_update_list(self, username: str, token: str, offset: Optional[int] = 0, limit: Optional[int] = 10) -> UserSubscriptionUpdateList:
        url = '/api/user/{username}/sub_update'.format(username=username)
        params = {'offset': offset, 'limit': limit}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserSubscriptionUpdateList)

    async def get_user_sub_update_list_by_username(self, username: str, token: str, offset: Optional[int] = 0, limit: Optional[int] = 10) -> UserSubscriptionUpdateList:
        url = '/api/user/by-username/{username}/sub_update'.format(username=username)
        params = {'offset': offset, 'limit': limit}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserSubscriptionUpdateList)

    async def get_user_sub_update_list_by_id(self, user_id: int, token: str, offset: Optional[int] = 0, limit: Optional[int] = 10) -> UserSubscriptionUpdateList:
        url = '/api/user/by-id/{user_id}/sub_update'.format(user_id=user_id)
        params = {'offset': offset, 'limit': limit}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserSubscriptionUpdateList)

    async def get_users(self, token: str, offset: Optional[int] = None, limit: Optional[int] = None, ids: Optional[List[int]] = None, username: Optional[List[str]] = None, usernames: Optional[List[str]] = None, admin: Optional[List[str]] = None, admin_ids: Optional[List[int]] = None, group: Optional[List[int]] = None, search: Optional[str] = None, status: Optional[Union[UserStatus, List[UserStatus]]] = None, sort: Optional[str] = None, proxy_id: Optional[str] = None, data_limit_reset_strategy: Optional[Union[DataLimitResetStrategy, List[DataLimitResetStrategy]]] = None, data_limit_min: Optional[int] = None, data_limit_max: Optional[int] = None, expire_after: Optional[datetime] = None, expire_before: Optional[datetime] = None, online_after: Optional[datetime] = None, online_before: Optional[datetime] = None, online: Optional[bool] = False, no_data_limit: Optional[bool] = False, no_expire: Optional[bool] = False, load_sub: Optional[bool] = False) -> UsersResponse:
        url = '/api/users'
        params = {'offset': offset, 'limit': limit, 'ids': ids, 'username': username, 'usernames': usernames, 'admin': admin, 'admin_ids': admin_ids, 'group': group, 'search': search, 'status': status, 'sort': sort, 'proxy_id': proxy_id, 'data_limit_reset_strategy': data_limit_reset_strategy, 'data_limit_min': data_limit_min, 'data_limit_max': data_limit_max, 'expire_after': expire_after, 'expire_before': expire_before, 'online_after': online_after, 'online_before': online_before, 'online': online, 'no_data_limit': no_data_limit, 'no_expire': no_expire, 'load_sub': load_sub}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UsersResponse)

    async def get_users_simple(self, token: str, ids: Optional[List[int]] = None, usernames: Optional[List[str]] = None, offset: Optional[int] = None, limit: Optional[int] = None, search: Optional[str] = None, sort: Optional[str] = None, all: Optional[bool] = False) -> UsersSimpleResponse:
        url = '/api/users/simple'
        params = {'ids': ids, 'usernames': usernames, 'offset': offset, 'limit': limit, 'search': search, 'sort': sort, 'all': all}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UsersSimpleResponse)

    async def get_user_usage(self, username: str, token: str, period: Optional[Period] = 'hour', node_id: Optional[int] = None, group_by_node: Optional[bool] = False, start: Optional[datetime] = None, end: Optional[datetime] = None) -> UserUsageStatsList:
        url = '/api/user/{username}/usage'.format(username=username)
        params = {'period': period, 'node_id': node_id, 'group_by_node': group_by_node, 'start': start, 'end': end}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserUsageStatsList)

    async def get_user_usage_by_username(self, username: str, token: str, period: Optional[Period] = 'hour', node_id: Optional[int] = None, group_by_node: Optional[bool] = False, start: Optional[datetime] = None, end: Optional[datetime] = None) -> UserUsageStatsList:
        url = '/api/user/by-username/{username}/usage'.format(username=username)
        params = {'period': period, 'node_id': node_id, 'group_by_node': group_by_node, 'start': start, 'end': end}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserUsageStatsList)

    async def get_user_usage_by_id(self, user_id: int, token: str, period: Optional[Period] = 'hour', node_id: Optional[int] = None, group_by_node: Optional[bool] = False, start: Optional[datetime] = None, end: Optional[datetime] = None) -> UserUsageStatsList:
        url = '/api/user/by-id/{user_id}/usage'.format(user_id=user_id)
        params = {'period': period, 'node_id': node_id, 'group_by_node': group_by_node, 'start': start, 'end': end}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserUsageStatsList)

    async def get_users_usage(self, token: str, period: Optional[Period] = 'hour', node_id: Optional[int] = None, group_by_node: Optional[bool] = False, start: Optional[datetime] = None, end: Optional[datetime] = None, admin: Optional[List[str]] = None) -> UserUsageStatsList:
        url = '/api/users/usage'
        params = {'period': period, 'node_id': node_id, 'group_by_node': group_by_node, 'start': start, 'end': end, 'admin': admin}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserUsageStatsList)

    async def get_users_count_metric(self, metric: UserCountMetric, token: str, period: Optional[Period] = 'hour', node_id: Optional[int] = None, group_by_node: Optional[bool] = False, start: Optional[datetime] = None, end: Optional[datetime] = None, admin: Optional[List[str]] = None) -> UserCountMetricStatsList:
        url = '/api/users/counts/{metric}'.format(metric=metric)
        params = {'period': period, 'node_id': node_id, 'group_by_node': group_by_node, 'start': start, 'end': end, 'admin': admin}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserCountMetricStatsList)

    async def get_expired_users(self, token: str, admin_username: Optional[str] = None, target: Optional[ExpiredUsersTarget] = "expired", expired_after: Optional[datetime] = None, expired_before: Optional[datetime] = None) -> List[str]:
        url = '/api/users/expired'
        params = {'admin_username': admin_username, 'target': target, 'expired_after': expired_after, 'expired_before': expired_before}
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, List[str])

    async def delete_expired_users(self, token: str, admin_username: Optional[str] = None, target: Optional[ExpiredUsersTarget] = "expired", expired_after: Optional[datetime] = None, expired_before: Optional[datetime] = None) -> RemoveUsersResponse:
        url = '/api/users/expired'
        params = {'admin_username': admin_username, 'target': target, 'expired_after': expired_after, 'expired_before': expired_before}
        headers = None
        response = await self._request('DELETE', url, token=token, params=params, headers=headers)
        return self._parse_response(response, RemoveUsersResponse)

    async def bulk_delete_users(self, bulk: BulkUsersSelection, token: str) -> RemoveUsersResponse:
        url = '/api/users/bulk/delete'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, RemoveUsersResponse)

    async def bulk_reset_users_data_usage(self, bulk: BulkUsersSelection, token: str) -> BulkUsersActionResponse:
        url = '/api/users/bulk/reset'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUsersActionResponse)

    async def bulk_disable_users(self, bulk: BulkUsersSelection, token: str) -> BulkUsersActionResponse:
        url = '/api/users/bulk/disable'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUsersActionResponse)

    async def bulk_enable_users(self, bulk: BulkUsersSelection, token: str) -> BulkUsersActionResponse:
        url = '/api/users/bulk/enable'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUsersActionResponse)

    async def bulk_revoke_users_subscription(self, bulk: BulkUsersSelection, token: str) -> BulkUsersActionResponse:
        url = '/api/users/bulk/revoke_sub'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersSelection)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUsersActionResponse)

    async def bulk_set_owner(self, bulk: BulkUsersSetOwner, token: str) -> BulkUsersActionResponse:
        url = '/api/users/bulk/set_owner'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersSetOwner)
        response = await self._request('PUT', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUsersActionResponse)

    async def create_user_from_template(self, template_user: CreateUserFromTemplate, token: str) -> UserResponse:
        url = '/api/user/from_template'
        params = None
        headers = None
        payload = self._validate_payload(template_user, CreateUserFromTemplate)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def bulk_create_users_from_template(self, bulk: BulkUsersFromTemplate, token: str) -> BulkUsersCreateResponse:
        url = '/api/users/bulk/from_template'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersFromTemplate)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUsersCreateResponse)

    async def bulk_apply_template_to_users(self, bulk: BulkUsersApplyTemplate, token: str) -> BulkUsersActionResponse:
        url = '/api/users/bulk/apply_template'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersApplyTemplate)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUsersActionResponse)

    async def modify_user_with_template(self, username: str, template_user: ModifyUserByTemplate, token: str) -> UserResponse:
        url = '/api/user/from_template/{username}'.format(username=username)
        params = None
        headers = None
        payload = self._validate_payload(template_user, ModifyUserByTemplate)
        response = await self._request('PUT', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def modify_user_with_template_by_username(self, username: str, template_user: ModifyUserByTemplate, token: str) -> UserResponse:
        url = '/api/user/from_template/by-username/{username}'.format(username=username)
        params = None
        headers = None
        payload = self._validate_payload(template_user, ModifyUserByTemplate)
        response = await self._request('PUT', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def modify_user_with_template_by_id(self, user_id: int, template_user: ModifyUserByTemplate, token: str) -> UserResponse:
        url = '/api/user/from_template/by-id/{user_id}'.format(user_id=user_id)
        params = None
        headers = None
        payload = self._validate_payload(template_user, ModifyUserByTemplate)
        response = await self._request('PUT', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def bulk_modify_users_expire(self, bulk: BulkUser, token: str) -> Any:
        url = '/api/users/bulk/expire'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUser)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def bulk_modify_users_datalimit(self, bulk: BulkUser, token: str) -> Any:
        url = '/api/users/bulk/data_limit'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUser)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def bulk_modify_users_proxy_settings(self, bulk: BulkUsersProxy, token: str) -> Any:
        url = '/api/users/bulk/proxy_settings'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersProxy)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def bulk_reallocate_wireguard_peer_ips(self, bulk: BulkWireGuardPeerIPs, token: str) -> WireGuardPeerIPsReallocateResponse:
        url = '/api/users/bulk/wireguard/reallocate-peer-ips'
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkWireGuardPeerIPs)
        response = await self._request('POST', url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, WireGuardPeerIPsReallocateResponse)

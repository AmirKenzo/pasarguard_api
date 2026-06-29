from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
    Literal,
)

from ..enums import (
    ConfigFormat,
    DataLimitResetStrategy,
    Period,
    UserCountMetric,
    UserStatus,
)
from ..models import (
    BulkUser,
    BulkUsersActionResponse,
    BulkUsersApplyTemplate,
    BulkUsersCreateResponse,
    BulkUsersFromTemplate,
    BulkUsersProxy,
    BulkUsersSelection,
    BulkUsersSetOwner,
    BulkWireGuardPeerIPs,
    CreateUserFromTemplate,
    ModifyUserByTemplate,
    RemoveUsersResponse,
    UserCountMetricStatsList,
    UserCreate,
    UserModify,
    UserResponse,
    UsersResponse,
    UsersSimpleResponse,
    UserStatusToggle,
    UserSubscriptionUpdateChart,
    UserSubscriptionUpdateList,
    UserUsageStatsList,
    WireGuardPeerIPsReallocateResponse,
)

ExpiredUsersTarget = Literal["expired", "limited"]


class UserMixin:
    async def create_user(self, user: UserCreate, token: str | None = None) -> UserResponse:
        url = "/api/user"
        params = None
        headers = None
        payload = self._validate_payload(user, UserCreate)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def create_user_in_all_groups(self, user: UserCreate, token: str | None = None) -> UserResponse:
        groups = await self.get_groups_simple(token=token, all=True)
        group_ids = [group.id for group in groups.groups]
        return await self.create_user(user.model_copy(update={"group_ids": group_ids}), token=token)

    async def modify_user(self, username: str, user: UserModify, token: str | None = None) -> UserResponse:
        url = f"/api/user/{username}"
        params = None
        headers = None
        payload = self._validate_payload(user, UserModify)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def remove_user(self, username: str, token: str | None = None) -> None:
        url = f"/api/user/{username}"
        params = None
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def get_user(self, username: str, token: str | None = None) -> UserResponse:
        url = f"/api/user/{username}"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def modify_user_by_username(self, username: str, user: UserModify, token: str | None = None) -> UserResponse:
        url = f"/api/user/by-username/{username}"
        params = None
        headers = None
        payload = self._validate_payload(user, UserModify)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def remove_user_by_username(self, username: str, token: str | None = None) -> None:
        url = f"/api/user/by-username/{username}"
        params = None
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def get_user_by_username(self, username: str, token: str | None = None) -> UserResponse:
        url = f"/api/user/by-username/{username}"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def modify_user_by_id(self, user_id: int, user: UserModify, token: str | None = None) -> UserResponse:
        url = f"/api/user/by-id/{user_id}"
        params = None
        headers = None
        payload = self._validate_payload(user, UserModify)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def remove_user_by_id(self, user_id: int, token: str | None = None) -> None:
        url = f"/api/user/by-id/{user_id}"
        params = None
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def get_user_by_id(self, user_id: int, token: str | None = None) -> UserResponse:
        url = f"/api/user/by-id/{user_id}"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def reset_user_data_usage(self, username: str, token: str | None = None) -> UserResponse:
        url = f"/api/user/{username}/reset"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def reset_user_data_usage_by_username(self, username: str, token: str | None = None) -> UserResponse:
        url = f"/api/user/by-username/{username}/reset"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def reset_user_data_usage_by_id(self, user_id: int, token: str | None = None) -> UserResponse:
        url = f"/api/user/by-id/{user_id}/reset"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def revoke_user_subscription(self, username: str, token: str | None = None) -> UserResponse:
        url = f"/api/user/{username}/revoke_sub"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def revoke_user_subscription_by_username(self, username: str, token: str | None = None) -> UserResponse:
        url = f"/api/user/by-username/{username}/revoke_sub"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def revoke_user_subscription_by_id(self, user_id: int, token: str | None = None) -> UserResponse:
        url = f"/api/user/by-id/{user_id}/revoke_sub"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def reset_users_data_usage(self, token: str | None = None) -> Any:
        url = "/api/users/reset"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def get_users_sub_update_chart(
        self,
        token: str | None = None,
        user_id: int | None = None,
        username: str | None = None,
        admin_id: int | None = None,
    ) -> UserSubscriptionUpdateChart:
        url = "/api/users/sub_update/chart"
        params = {"user_id": user_id, "username": username, "admin_id": admin_id}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserSubscriptionUpdateChart)

    async def set_owner(self, username: str, admin_username: str, token: str | None = None) -> UserResponse:
        url = f"/api/user/{username}/set_owner"
        params = {"admin_username": admin_username}
        headers = None
        response = await self._request("PUT", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def set_owner_by_username(self, username: str, admin_username: str, token: str | None = None) -> UserResponse:
        url = f"/api/user/by-username/{username}/set_owner"
        params = {"admin_username": admin_username}
        headers = None
        response = await self._request("PUT", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def set_owner_by_id(self, user_id: int, admin_username: str, token: str | None = None) -> UserResponse:
        url = f"/api/user/by-id/{user_id}/set_owner"
        params = {"admin_username": admin_username}
        headers = None
        response = await self._request("PUT", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def active_next_plan(self, username: str, token: str | None = None) -> UserResponse:
        url = f"/api/user/{username}/active_next"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def active_next_plan_by_username(self, username: str, token: str | None = None) -> UserResponse:
        url = f"/api/user/by-username/{username}/active_next"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def active_next_plan_by_id(self, user_id: int, token: str | None = None) -> UserResponse:
        url = f"/api/user/by-id/{user_id}/active_next"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def get_user_subscription_by_id(
        self, user_id: int, client_type: ConfigFormat, token: str | None = None
    ) -> Any:
        url = f"/api/user/{user_id}/subscription/{client_type}"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def get_user_sub_update_list(
        self, username: str, token: str | None = None, offset: int | None = 0, limit: int | None = 10
    ) -> UserSubscriptionUpdateList:
        url = f"/api/user/{username}/sub_update"
        params = {"offset": offset, "limit": limit}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserSubscriptionUpdateList)

    async def get_user_sub_update_list_by_username(
        self, username: str, token: str | None = None, offset: int | None = 0, limit: int | None = 10
    ) -> UserSubscriptionUpdateList:
        url = f"/api/user/by-username/{username}/sub_update"
        params = {"offset": offset, "limit": limit}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserSubscriptionUpdateList)

    async def get_user_sub_update_list_by_id(
        self, user_id: int, token: str | None = None, offset: int | None = 0, limit: int | None = 10
    ) -> UserSubscriptionUpdateList:
        url = f"/api/user/by-id/{user_id}/sub_update"
        params = {"offset": offset, "limit": limit}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserSubscriptionUpdateList)

    async def get_users(
        self,
        token: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        ids: list[int] | None = None,
        username: list[str] | None = None,
        usernames: list[str] | None = None,
        admin: list[str] | None = None,
        admin_ids: list[int] | None = None,
        group: list[int] | None = None,
        search: str | None = None,
        status: UserStatus | list[UserStatus] | None = None,
        sort: str | None = None,
        proxy_id: str | None = None,
        data_limit_reset_strategy: DataLimitResetStrategy | list[DataLimitResetStrategy] | None = None,
        data_limit_min: int | None = None,
        data_limit_max: int | None = None,
        expire_after: datetime | None = None,
        expire_before: datetime | None = None,
        online_after: datetime | None = None,
        online_before: datetime | None = None,
        online: bool | None = False,
        no_data_limit: bool | None = False,
        no_expire: bool | None = False,
        load_sub: bool | None = False,
    ) -> UsersResponse:
        url = "/api/users"
        params = {
            "offset": offset,
            "limit": limit,
            "ids": ids,
            "username": username,
            "usernames": usernames,
            "admin": admin,
            "admin_ids": admin_ids,
            "group": group,
            "search": search,
            "status": status,
            "sort": sort,
            "proxy_id": proxy_id,
            "data_limit_reset_strategy": data_limit_reset_strategy,
            "data_limit_min": data_limit_min,
            "data_limit_max": data_limit_max,
            "expire_after": expire_after,
            "expire_before": expire_before,
            "online_after": online_after,
            "online_before": online_before,
            "online": online,
            "no_data_limit": no_data_limit,
            "no_expire": no_expire,
            "load_sub": load_sub,
        }
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UsersResponse)

    async def get_users_simple(
        self,
        token: str | None = None,
        ids: list[int] | None = None,
        usernames: list[str] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        search: str | None = None,
        sort: str | None = None,
        all: bool | None = False,
    ) -> UsersSimpleResponse:
        url = "/api/users/simple"
        params = {
            "ids": ids,
            "usernames": usernames,
            "offset": offset,
            "limit": limit,
            "search": search,
            "sort": sort,
            "all": all,
        }
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UsersSimpleResponse)

    async def get_user_usage(
        self,
        username: str,
        token: str | None = None,
        period: Period | None = "hour",
        node_id: int | None = None,
        group_by_node: bool | None = False,
        start: datetime | None = None,
        end: datetime | None = None,
    ) -> UserUsageStatsList:
        url = f"/api/user/{username}/usage"
        params = {"period": period, "node_id": node_id, "group_by_node": group_by_node, "start": start, "end": end}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserUsageStatsList)

    async def get_user_usage_by_username(
        self,
        username: str,
        token: str | None = None,
        period: Period | None = "hour",
        node_id: int | None = None,
        group_by_node: bool | None = False,
        start: datetime | None = None,
        end: datetime | None = None,
    ) -> UserUsageStatsList:
        url = f"/api/user/by-username/{username}/usage"
        params = {"period": period, "node_id": node_id, "group_by_node": group_by_node, "start": start, "end": end}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserUsageStatsList)

    async def get_user_usage_by_id(
        self,
        user_id: int,
        token: str | None = None,
        period: Period | None = "hour",
        node_id: int | None = None,
        group_by_node: bool | None = False,
        start: datetime | None = None,
        end: datetime | None = None,
    ) -> UserUsageStatsList:
        url = f"/api/user/by-id/{user_id}/usage"
        params = {"period": period, "node_id": node_id, "group_by_node": group_by_node, "start": start, "end": end}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserUsageStatsList)

    async def get_users_usage(
        self,
        token: str | None = None,
        period: Period | None = "hour",
        node_id: int | None = None,
        group_by_node: bool | None = False,
        start: datetime | None = None,
        end: datetime | None = None,
        admin: list[str] | None = None,
    ) -> UserUsageStatsList:
        url = "/api/users/usage"
        params = {
            "period": period,
            "node_id": node_id,
            "group_by_node": group_by_node,
            "start": start,
            "end": end,
            "admin": admin,
        }
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserUsageStatsList)

    async def get_users_count_metric(
        self,
        metric: UserCountMetric,
        token: str | None = None,
        period: Period | None = "hour",
        node_id: int | None = None,
        group_by_node: bool | None = False,
        start: datetime | None = None,
        end: datetime | None = None,
        admin: list[str] | None = None,
    ) -> UserCountMetricStatsList:
        url = f"/api/users/counts/{metric}"
        params = {
            "period": period,
            "node_id": node_id,
            "group_by_node": group_by_node,
            "start": start,
            "end": end,
            "admin": admin,
        }
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserCountMetricStatsList)

    async def get_expired_users(
        self,
        token: str | None = None,
        admin_username: str | None = None,
        target: ExpiredUsersTarget | None = "expired",
        expired_after: datetime | None = None,
        expired_before: datetime | None = None,
    ) -> list[str]:
        url = "/api/users/expired"
        params = {
            "admin_username": admin_username,
            "target": target,
            "expired_after": expired_after,
            "expired_before": expired_before,
        }
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, list[str])

    async def delete_expired_users(
        self,
        token: str | None = None,
        admin_username: str | None = None,
        target: ExpiredUsersTarget | None = "expired",
        expired_after: datetime | None = None,
        expired_before: datetime | None = None,
    ) -> RemoveUsersResponse:
        url = "/api/users/expired"
        params = {
            "admin_username": admin_username,
            "target": target,
            "expired_after": expired_after,
            "expired_before": expired_before,
        }
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, RemoveUsersResponse)

    async def bulk_delete_users(self, bulk: BulkUsersSelection, token: str | None = None) -> RemoveUsersResponse:
        url = "/api/users/bulk/delete"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, RemoveUsersResponse)

    async def bulk_reset_users_data_usage(
        self, bulk: BulkUsersSelection, token: str | None = None
    ) -> BulkUsersActionResponse:
        url = "/api/users/bulk/reset"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUsersActionResponse)

    async def bulk_disable_users(self, bulk: BulkUsersSelection, token: str | None = None) -> BulkUsersActionResponse:
        url = "/api/users/bulk/disable"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUsersActionResponse)

    async def bulk_enable_users(self, bulk: BulkUsersSelection, token: str | None = None) -> BulkUsersActionResponse:
        url = "/api/users/bulk/enable"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUsersActionResponse)

    async def bulk_revoke_users_subscription(
        self, bulk: BulkUsersSelection, token: str | None = None
    ) -> BulkUsersActionResponse:
        url = "/api/users/bulk/revoke_sub"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUsersActionResponse)

    async def bulk_set_owner(self, bulk: BulkUsersSetOwner, token: str | None = None) -> BulkUsersActionResponse:
        url = "/api/users/bulk/set_owner"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersSetOwner)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUsersActionResponse)

    async def create_user_from_template(
        self, template_user: CreateUserFromTemplate, token: str | None = None
    ) -> UserResponse:
        url = "/api/user/from_template"
        params = None
        headers = None
        payload = self._validate_payload(template_user, CreateUserFromTemplate)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def bulk_create_users_from_template(
        self, bulk: BulkUsersFromTemplate, token: str | None = None
    ) -> BulkUsersCreateResponse:
        url = "/api/users/bulk/from_template"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersFromTemplate)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUsersCreateResponse)

    async def bulk_apply_template_to_users(
        self, bulk: BulkUsersApplyTemplate, token: str | None = None
    ) -> BulkUsersActionResponse:
        url = "/api/users/bulk/apply_template"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersApplyTemplate)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkUsersActionResponse)

    async def modify_user_with_template(
        self, username: str, template_user: ModifyUserByTemplate, token: str | None = None
    ) -> UserResponse:
        url = f"/api/user/from_template/{username}"
        params = None
        headers = None
        payload = self._validate_payload(template_user, ModifyUserByTemplate)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def modify_user_with_template_by_username(
        self, username: str, template_user: ModifyUserByTemplate, token: str | None = None
    ) -> UserResponse:
        url = f"/api/user/from_template/by-username/{username}"
        params = None
        headers = None
        payload = self._validate_payload(template_user, ModifyUserByTemplate)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def modify_user_with_template_by_id(
        self, user_id: int, template_user: ModifyUserByTemplate, token: str | None = None
    ) -> UserResponse:
        url = f"/api/user/from_template/by-id/{user_id}"
        params = None
        headers = None
        payload = self._validate_payload(template_user, ModifyUserByTemplate)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def bulk_modify_users_expire(self, bulk: BulkUser, token: str | None = None) -> Any:
        url = "/api/users/bulk/expire"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUser)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def bulk_modify_users_datalimit(self, bulk: BulkUser, token: str | None = None) -> Any:
        url = "/api/users/bulk/data_limit"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUser)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def bulk_modify_users_proxy_settings(self, bulk: BulkUsersProxy, token: str | None = None) -> Any:
        url = "/api/users/bulk/proxy_settings"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkUsersProxy)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def bulk_reallocate_wireguard_peer_ips(
        self, bulk: BulkWireGuardPeerIPs, token: str | None = None
    ) -> WireGuardPeerIPsReallocateResponse:
        url = "/api/users/bulk/wireguard/reallocate-peer-ips"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkWireGuardPeerIPs)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, WireGuardPeerIPsReallocateResponse)

    async def set_user_disabled(
        self, username: str, status: UserStatusToggle, token: str | None = None
    ) -> UserResponse:
        url = f"/api/user/{username}/disabled"
        params = None
        headers = None
        payload = self._validate_payload(status, UserStatusToggle)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def set_user_disabled_by_username(
        self, username: str, status: UserStatusToggle, token: str | None = None
    ) -> UserResponse:
        url = f"/api/user/by-username/{username}/disabled"
        params = None
        headers = None
        payload = self._validate_payload(status, UserStatusToggle)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

    async def set_user_disabled_by_id(
        self, user_id: int, status: UserStatusToggle, token: str | None = None
    ) -> UserResponse:
        url = f"/api/user/by-id/{user_id}/disabled"
        params = None
        headers = None
        payload = self._validate_payload(status, UserStatusToggle)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, UserResponse)

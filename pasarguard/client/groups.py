from __future__ import annotations

from typing import (
    Any,
)

from ..models import (
    BulkGroup,
    BulkGroupsActionResponse,
    BulkGroupSelection,
    GroupCreate,
    GroupModify,
    GroupResponse,
    GroupsResponse,
    GroupsSimpleResponse,
    RemoveGroupsResponse,
)


class GroupsMixin:
    async def create_group(self, group: GroupCreate, token: str | None = None) -> GroupResponse:
        url = "/api/group"
        params = None
        headers = None
        payload = self._validate_payload(group, GroupCreate)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, GroupResponse)

    async def get_all_groups(
        self,
        token: str | None = None,
        ids: list[int] | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> GroupsResponse:
        url = "/api/groups"
        params = {"ids": ids, "offset": offset, "limit": limit}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, GroupsResponse)

    async def get_groups_simple(
        self,
        token: str | None = None,
        ids: list[int] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        search: str | None = None,
        sort: str | None = None,
        all: bool | None = False,
    ) -> GroupsSimpleResponse:
        url = "/api/groups/simple"
        params = {"ids": ids, "offset": offset, "limit": limit, "search": search, "sort": sort, "all": all}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, GroupsSimpleResponse)

    async def get_group(self, group_id: int, token: str | None = None) -> GroupResponse:
        url = f"/api/group/{group_id}"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, GroupResponse)

    async def modify_group(self, group_id: int, group: GroupModify, token: str | None = None) -> GroupResponse:
        url = f"/api/group/{group_id}"
        params = None
        headers = None
        payload = self._validate_payload(group, GroupModify)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, GroupResponse)

    async def remove_group(self, group_id: int, token: str | None = None) -> None:
        url = f"/api/group/{group_id}"
        params = None
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def bulk_add_groups_to_users(self, bulk: BulkGroup, token: str | None = None) -> Any:
        url = "/api/groups/bulk/add"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkGroup)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def bulk_remove_users_from_groups(self, bulk: BulkGroup, token: str | None = None) -> Any:
        url = "/api/groups/bulk/remove"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkGroup)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def bulk_delete_groups(self, bulk: BulkGroupSelection, token: str | None = None) -> RemoveGroupsResponse:
        url = "/api/groups/bulk/delete"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkGroupSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, RemoveGroupsResponse)

    async def bulk_disable_groups(self, bulk: BulkGroupSelection, token: str | None = None) -> BulkGroupsActionResponse:
        url = "/api/groups/bulk/disable"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkGroupSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkGroupsActionResponse)

    async def bulk_enable_groups(self, bulk: BulkGroupSelection, token: str | None = None) -> BulkGroupsActionResponse:
        url = "/api/groups/bulk/enable"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkGroupSelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, BulkGroupsActionResponse)

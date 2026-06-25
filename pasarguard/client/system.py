from __future__ import annotations

from ._imports import (
    InboundSummary,
    List,
    Optional,
    SystemResourceStats,
    SystemStats,
    SystemUsersStats,
    WorkersHealth,
)


class SystemMixin:
    async def get_system_stats(self, token: str, admin_username: Optional[str] = None) -> SystemStats:
        url = "/api/system"
        params = {"admin_username": admin_username}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, SystemStats)

    async def get_system_users_stats(self, token: str, admin_username: Optional[str] = None) -> SystemUsersStats:
        url = "/api/system/users"
        params = {"admin_username": admin_username}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, SystemUsersStats)

    async def get_system_resource_stats(self, token: str) -> SystemResourceStats:
        url = "/api/system/resources"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, SystemResourceStats)

    async def get_inbounds(self, token: str) -> List[str]:
        url = "/api/inbounds"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, List[str])

    async def get_inbound_details(self, token: str) -> List[InboundSummary]:
        url = "/api/inbounds/details"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, List[InboundSummary])

    async def get_workers_health(self, token: str) -> WorkersHealth:
        url = "/api/workers/health"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, WorkersHealth)

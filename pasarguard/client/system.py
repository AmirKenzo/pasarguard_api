from __future__ import annotations

from ..models import (
    InboundSummary,
    SystemResourceStats,
    SystemStats,
    SystemUsersStats,
    WorkersHealth,
)


class SystemMixin:
    async def get_system_stats(self, token: str, admin_username: str | None = None) -> SystemStats:
        url = "/api/system"
        params = {"admin_username": admin_username}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, SystemStats)

    async def get_system_users_stats(self, token: str, admin_username: str | None = None) -> SystemUsersStats:
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

    async def get_inbounds(self, token: str) -> list[str]:
        url = "/api/inbounds"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, list[str])

    async def get_inbound_details(self, token: str) -> list[InboundSummary]:
        url = "/api/inbounds/details"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, list[InboundSummary])

    async def get_workers_health(self, token: str) -> WorkersHealth:
        url = "/api/workers/health"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, WorkersHealth)

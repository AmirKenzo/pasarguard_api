from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
)

from ..enums import (
    ConfigFormat,
    GeoFilseRegion,
    Period,
)
from ..models import (
    NodeCoreUpdate,
    NodeGeoFilesUpdate,
    SubscriptionUserResponse,
    UserCreate,
    UserResponse,
    UserUsageStatsList,
)


class CompatibilityMixin:
    async def add_user(self, user: UserCreate, token: str | None = None) -> UserResponse:
        return await self.create_user(user=user, token=token)

    async def activate_next_plan(self, username: str, token: str | None = None) -> UserResponse:
        return await self.active_next_plan(username=username, token=token)

    async def get_user_data_usage(
        self,
        username: str,
        token: str | None = None,
        start_date: datetime | None = None,
        end_date: datetime | None = None,
        period: Period = Period.HOUR,
    ) -> UserUsageStatsList:
        return await self.get_user_usage(username=username, token=token, start=start_date, end=end_date, period=period)

    async def update_node_core(self, node_id: int, core_version: str, token: str | None = None) -> Any:
        return await self.update_core(
            node_id=node_id,
            node_core_update=NodeCoreUpdate(core_version=core_version),
            token=token,
        )

    async def update_node_geofiles(self, node_id: int, region: GeoFilseRegion | str, token: str | None = None) -> Any:
        return await self.update_geofiles(
            node_id=node_id,
            node_geo_files_update=NodeGeoFilesUpdate(region=region),
            token=token,
        )

    async def get_user_subscription_info(
        self, url: str | None = None, token: str | None = None
    ) -> SubscriptionUserResponse:
        if url:
            response = await self._request("GET", url.rstrip("/") + "/info", authenticated=False)
            return self._parse_response(response, SubscriptionUserResponse)
        if token:
            return await self.user_subscription_info(token=token)
        raise ValueError("Either url or token must be provided")

    async def get_sub_user_usage_by_url(
        self,
        url: str | None = None,
        token: str | None = None,
        period: Period = Period.HOUR,
        start: datetime | None = None,
        end: datetime | None = None,
    ) -> UserUsageStatsList:
        if url:
            response = await self._request(
                "GET",
                url.rstrip("/") + "/usage",
                authenticated=False,
                params={"period": period, "start": start, "end": end},
            )
            return self._parse_response(response, UserUsageStatsList)
        if token:
            return await self.get_sub_user_usage(token=token, period=period, start=start, end=end)
        raise ValueError("Either url or token must be provided")

    async def get_user_subscription_with_client_type(
        self, client_type: ConfigFormat | str, url: str | None = None, token: str | None = None, **headers: Any
    ) -> list[str]:
        if url:
            response = await self._request(
                "GET",
                url.rstrip("/") + f"/{self._serialize(client_type)}",
                authenticated=False,
                headers=headers,
            )
            content = response.text
        elif token:
            result = await self.user_subscription_with_client_type(token=token, client_type=client_type, **headers)
            content = result if isinstance(result, str) else str(result)
        else:
            raise ValueError("Either url or token must be provided")
        return [line for line in content.strip().splitlines() if line and "@0.0.0.0:" not in line]

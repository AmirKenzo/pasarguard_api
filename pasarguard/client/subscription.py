from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
)

from ..enums import (
    ConfigFormat,
    Period,
)
from ..models import (
    Application,
    SubscriptionUserResponse,
    UserUsageStatsList,
)


class SubscriptionMixin:
    async def user_subscription(
        self,
        token: str,
        user_agent: str | None = "",
        x_h_w_i_d: str | None = None,
        x_device_o_s: str | None = None,
        x_ver_o_s: str | None = None,
        x_device_model: str | None = None,
    ) -> Any:
        url = f"/sub/{token}/"
        params = None
        headers = {
            "user-agent": user_agent,
            "X-HWID": x_h_w_i_d,
            "X-Device-OS": x_device_o_s,
            "X-Ver-OS": x_ver_o_s,
            "X-Device-Model": x_device_model,
        }
        response = await self._request("GET", url, token=None, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def user_subscription_info(self, token: str) -> SubscriptionUserResponse:
        url = f"/sub/{token}/info"
        params = None
        headers = None
        response = await self._request("GET", url, token=None, params=params, headers=headers)
        return self._parse_response(response, SubscriptionUserResponse)

    async def user_subscription_raw(
        self,
        token: str,
        x_subscription_user_agent: str | None = "",
        x_h_w_i_d: str | None = None,
        x_device_o_s: str | None = None,
        x_ver_o_s: str | None = None,
        x_device_model: str | None = None,
    ) -> Any:
        url = f"/sub/{token}/raw"
        params = None
        headers = {
            "X-Subscription-User-Agent": x_subscription_user_agent,
            "X-HWID": x_h_w_i_d,
            "X-Device-OS": x_device_o_s,
            "X-Ver-OS": x_ver_o_s,
            "X-Device-Model": x_device_model,
        }
        response = await self._request("GET", url, token=None, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def user_subscription_apps(self, token: str) -> list[Application]:
        url = f"/sub/{token}/apps"
        params = None
        headers = None
        response = await self._request("GET", url, token=None, params=params, headers=headers)
        return self._parse_response(response, list[Application])

    async def get_sub_user_usage(
        self,
        token: str,
        period: Period | None = "hour",
        start: datetime | None = None,
        end: datetime | None = None,
    ) -> UserUsageStatsList:
        url = f"/sub/{token}/usage"
        params = {"period": period, "start": start, "end": end}
        headers = None
        response = await self._request("GET", url, token=None, params=params, headers=headers)
        return self._parse_response(response, UserUsageStatsList)

    async def user_subscription_with_client_type(
        self,
        token: str,
        client_type: ConfigFormat,
        x_h_w_i_d: str | None = None,
        x_device_o_s: str | None = None,
        x_ver_o_s: str | None = None,
        x_device_model: str | None = None,
    ) -> Any:
        url = f"/sub/{token}/{client_type}"
        params = None
        headers = {
            "X-HWID": x_h_w_i_d,
            "X-Device-OS": x_device_o_s,
            "X-Ver-OS": x_ver_o_s,
            "X-Device-Model": x_device_model,
        }
        response = await self._request("GET", url, token=None, params=params, headers=headers)
        return self._parse_response(response, Any)

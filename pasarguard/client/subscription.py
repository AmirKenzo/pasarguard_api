from __future__ import annotations

from ._imports import (
    Any,
    Application,
    ConfigFormat,
    List,
    Optional,
    Period,
    SubscriptionUserResponse,
    UserUsageStatsList,
    datetime,
)


class SubscriptionMixin:
    async def user_subscription(
        self,
        token: str,
        user_agent: Optional[str] = "",
        x_h_w_i_d: Optional[str] = None,
        x_device_o_s: Optional[str] = None,
        x_ver_o_s: Optional[str] = None,
        x_device_model: Optional[str] = None,
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
        x_subscription_user_agent: Optional[str] = "",
        x_h_w_i_d: Optional[str] = None,
        x_device_o_s: Optional[str] = None,
        x_ver_o_s: Optional[str] = None,
        x_device_model: Optional[str] = None,
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

    async def user_subscription_apps(self, token: str) -> List[Application]:
        url = f"/sub/{token}/apps"
        params = None
        headers = None
        response = await self._request("GET", url, token=None, params=params, headers=headers)
        return self._parse_response(response, List[Application])

    async def get_sub_user_usage(
        self,
        token: str,
        period: Optional[Period] = "hour",
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
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
        x_h_w_i_d: Optional[str] = None,
        x_device_o_s: Optional[str] = None,
        x_ver_o_s: Optional[str] = None,
        x_device_model: Optional[str] = None,
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

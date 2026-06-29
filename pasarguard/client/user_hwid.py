from __future__ import annotations

from typing import Any

from ..models import UserHWIDListResponse


class UserHWIDMixin:
    async def get_user_hwids(self, user_id: int, token: str | None = None) -> UserHWIDListResponse:
        url = f"/api/user/{user_id}/hwids"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserHWIDListResponse)

    async def delete_user_hwid(self, user_id: int, hwid: str, token: str | None = None) -> Any:
        url = f"/api/user/{user_id}/hwids/{hwid}"
        params = None
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def reset_user_hwids(self, user_id: int, token: str | None = None) -> Any:
        url = f"/api/user/{user_id}/hwids/reset"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

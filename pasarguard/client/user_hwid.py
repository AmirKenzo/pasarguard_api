from __future__ import annotations

from ._imports import (
    Any,
    UserHWIDListResponse,
)


class UserHWIDMixin:
    async def get_user_hwids(self, user_id: int, token: str) -> UserHWIDListResponse:
        url = '/api/user/{user_id}/hwids'.format(user_id=user_id)
        params = None
        headers = None
        response = await self._request('GET', url, token=token, params=params, headers=headers)
        return self._parse_response(response, UserHWIDListResponse)

    async def delete_user_hwid(self, user_id: int, hwid: str, token: str) -> Any:
        url = '/api/user/{user_id}/hwids/{hwid}'.format(user_id=user_id, hwid=hwid)
        params = None
        headers = None
        response = await self._request('DELETE', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

    async def reset_user_hwids(self, user_id: int, token: str) -> Any:
        url = '/api/user/{user_id}/hwids/reset'.format(user_id=user_id)
        params = None
        headers = None
        response = await self._request('POST', url, token=token, params=params, headers=headers)
        return self._parse_response(response, Any)

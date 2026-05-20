from __future__ import annotations

from ._imports import (
    Any,
    Dict,
)


class DefaultMixin:
    async def base(self) -> str:
        url = '/'
        params = None
        headers = None
        response = await self._request('GET', url, token=None, params=params, headers=headers)
        return self._parse_response(response, str)

    async def health(self) -> Dict[str, Any]:
        url = '/health'
        params = None
        headers = None
        response = await self._request('GET', url, token=None, params=params, headers=headers)
        return self._parse_response(response, Dict[str, Any])

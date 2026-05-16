from __future__ import annotations

# ruff: noqa: F401, F403
from ._imports import *


class DefaultMixin:
    async def health(self) -> Dict[str, Any]:
        url = '/health'
        params = None
        headers = None
        response = await self._request('GET', url, token=None, params=params, headers=headers)
        return self._parse_response(response, Dict[str, Any])

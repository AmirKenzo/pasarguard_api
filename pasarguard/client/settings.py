from __future__ import annotations

from ._imports import (
    General,
    SettingsSchema,
)


class SettingsMixin:
    async def get_settings(self, token: str) -> SettingsSchema:
        url = "/api/settings"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, SettingsSchema)

    async def modify_settings(self, settings: SettingsSchema, token: str) -> SettingsSchema:
        url = "/api/settings"
        params = None
        headers = None
        payload = self._validate_payload(settings, SettingsSchema)
        response = await self._request("PUT", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, SettingsSchema)

    async def get_general_settings(self, token: str) -> General:
        url = "/api/settings/general"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, General)

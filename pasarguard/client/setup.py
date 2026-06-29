from __future__ import annotations

from ..models import (
    AdminDetails,
    OwnerCreateRequest,
    OwnerResetRequest,
    OwnerUpgradeRequest,
)


class SetupMixin:
    async def create_owner(self, request: OwnerCreateRequest) -> AdminDetails:
        url = "/api/setup/owner"
        params = None
        headers = None
        payload = self._validate_payload(request, OwnerCreateRequest)
        response = await self._request(
            "POST", url, authenticated=False, json_data=payload, params=params, headers=headers
        )
        return self._parse_response(response, AdminDetails)

    async def delete_owner(self, key: str) -> None:
        url = "/api/setup/owner"
        params = {"key": key}
        headers = None
        response = await self._request("DELETE", url, authenticated=False, params=params, headers=headers)
        return self._parse_response(response, None)

    async def upgrade_owner(self, request: OwnerUpgradeRequest) -> AdminDetails:
        url = "/api/setup/owner/upgrade"
        params = None
        headers = None
        payload = self._validate_payload(request, OwnerUpgradeRequest)
        response = await self._request(
            "POST", url, authenticated=False, json_data=payload, params=params, headers=headers
        )
        return self._parse_response(response, AdminDetails)

    async def reset_owner_password(self, request: OwnerResetRequest) -> AdminDetails:
        url = "/api/setup/owner"
        params = None
        headers = None
        payload = self._validate_payload(request, OwnerResetRequest)
        response = await self._request(
            "PATCH", url, authenticated=False, json_data=payload, params=params, headers=headers
        )
        return self._parse_response(response, AdminDetails)

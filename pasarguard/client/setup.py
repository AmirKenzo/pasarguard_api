from __future__ import annotations

from ._imports import (
    AdminDetails,
    OwnerCreateRequest,
    OwnerDeleteRequest,
    OwnerResetRequest,
)


class SetupMixin:
    async def create_owner(self, request: OwnerCreateRequest) -> AdminDetails:
        url = "/api/setup/owner"
        params = None
        headers = None
        payload = self._validate_payload(request, OwnerCreateRequest)
        response = await self._request("POST", url, token=None, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

    async def delete_owner(self, request: OwnerDeleteRequest) -> None:
        url = "/api/setup/owner"
        params = None
        headers = None
        payload = self._validate_payload(request, OwnerDeleteRequest)
        response = await self._request("DELETE", url, token=None, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, None)

    async def reset_owner_password(self, request: OwnerResetRequest) -> AdminDetails:
        url = "/api/setup/owner"
        params = None
        headers = None
        payload = self._validate_payload(request, OwnerResetRequest)
        response = await self._request("PATCH", url, token=None, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, AdminDetails)

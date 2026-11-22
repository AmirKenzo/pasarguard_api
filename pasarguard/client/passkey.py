from __future__ import annotations

from typing import Any

from ..models import (
    PasskeyAuthenticationRequest,
    PasskeyInfo,
    PasskeyOptionsRequest,
    PasskeyRegistrationRequest,
    Token,
)


class PasskeyMixin:
    async def passkey_login_options(self, body: PasskeyOptionsRequest | None = None) -> Any:
        """Get WebAuthn assertion options for passkey login (unauthenticated)."""
        url = "/api/admin/passkey/login/options"
        payload = self._validate_payload(body or PasskeyOptionsRequest(), PasskeyOptionsRequest)
        response = await self._request("POST", url, json_data=payload, authenticated=False)
        return self._parse_response(response, Any)

    async def passkey_login_verify(self, body: PasskeyAuthenticationRequest) -> Token:
        """Verify a WebAuthn assertion and issue an admin token (unauthenticated)."""
        url = "/api/admin/passkey/login/verify"
        payload = self._validate_payload(body, PasskeyAuthenticationRequest)
        response = await self._request("POST", url, json_data=payload, authenticated=False)
        return self._parse_response(response, Token)

    async def list_passkeys(self, token: str | None = None) -> list[PasskeyInfo]:
        url = "/api/admin/passkey"
        response = await self._request("GET", url, token=token)
        return self._parse_response(response, list[PasskeyInfo])

    async def passkey_register_options(self, token: str | None = None) -> Any:
        url = "/api/admin/passkey/register/options"
        response = await self._request("POST", url, token=token)
        return self._parse_response(response, Any)

    async def passkey_register_verify(self, body: PasskeyRegistrationRequest, token: str | None = None) -> Any:
        url = "/api/admin/passkey/register/verify"
        payload = self._validate_payload(body, PasskeyRegistrationRequest)
        response = await self._request("POST", url, token=token, json_data=payload)
        return self._parse_response(response, Any)

    async def delete_passkey(self, passkey_id: int, token: str | None = None) -> Any:
        url = f"/api/admin/passkey/{passkey_id}"
        response = await self._request("DELETE", url, token=token)
        return self._parse_response(response, Any)

    async def list_admin_passkeys(self, admin_id: int, token: str | None = None) -> list[PasskeyInfo]:
        url = f"/api/admin/passkey/admins/{admin_id}"
        response = await self._request("GET", url, token=token)
        return self._parse_response(response, list[PasskeyInfo])

    async def admin_passkey_register_options(self, admin_id: int, token: str | None = None) -> Any:
        url = f"/api/admin/passkey/admins/{admin_id}/register/options"
        response = await self._request("POST", url, token=token)
        return self._parse_response(response, Any)

    async def admin_passkey_register_verify(
        self, admin_id: int, body: PasskeyRegistrationRequest, token: str | None = None
    ) -> Any:
        url = f"/api/admin/passkey/admins/{admin_id}/register/verify"
        payload = self._validate_payload(body, PasskeyRegistrationRequest)
        response = await self._request("POST", url, token=token, json_data=payload)
        return self._parse_response(response, Any)

    async def delete_admin_passkey(self, admin_id: int, passkey_id: int, token: str | None = None) -> Any:
        url = f"/api/admin/passkey/admins/{admin_id}/{passkey_id}"
        response = await self._request("DELETE", url, token=token)
        return self._parse_response(response, Any)

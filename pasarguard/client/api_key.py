from __future__ import annotations

from ..enums.api_key import APIKeyStatus
from ..models import (
    APIKeyCreate,
    APIKeyCreateResponse,
    APIKeyResponse,
    APIKeysResponse,
    APIKeyUpdate,
    BulkAPIKeySelection,
    RemoveAPIKeysResponse,
)


class ApiKeyMixin:
    async def create_api_key(self, api_key: APIKeyCreate, token: str | None = None) -> APIKeyCreateResponse:
        url = "/api/api_key"
        params = None
        headers = None
        payload = self._validate_payload(api_key, APIKeyCreate)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, APIKeyCreateResponse)

    async def get_api_key(self, key_id: int, token: str | None = None) -> APIKeyResponse:
        url = f"/api/api_key/{key_id}"
        params = None
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, APIKeyResponse)

    async def modify_api_key(self, key_id: int, api_key: APIKeyUpdate, token: str | None = None) -> APIKeyResponse:
        url = f"/api/api_key/{key_id}"
        params = None
        headers = None
        payload = self._validate_payload(api_key, APIKeyUpdate)
        response = await self._request("PATCH", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, APIKeyResponse)

    async def remove_api_key(self, key_id: int, token: str | None = None) -> None:
        url = f"/api/api_key/{key_id}"
        params = None
        headers = None
        response = await self._request("DELETE", url, token=token, params=params, headers=headers)
        return self._parse_response(response, None)

    async def revoke_api_key(self, key_id: int, token: str | None = None) -> APIKeyCreateResponse:
        url = f"/api/api_key/{key_id}/revoke"
        params = None
        headers = None
        response = await self._request("POST", url, token=token, params=params, headers=headers)
        return self._parse_response(response, APIKeyCreateResponse)

    async def list_api_keys(
        self,
        token: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        key_id: int | None = None,
        name: str | None = None,
        status: APIKeyStatus | None = None,
    ) -> APIKeysResponse:
        url = "/api/api_keys"
        params = {"offset": offset, "limit": limit, "key_id": key_id, "name": name, "status": status}
        headers = None
        response = await self._request("GET", url, token=token, params=params, headers=headers)
        return self._parse_response(response, APIKeysResponse)

    async def bulk_delete_api_keys(self, bulk: BulkAPIKeySelection, token: str | None = None) -> RemoveAPIKeysResponse:
        url = "/api/api_keys/bulk/delete"
        params = None
        headers = None
        payload = self._validate_payload(bulk, BulkAPIKeySelection)
        response = await self._request("POST", url, token=token, json_data=payload, params=params, headers=headers)
        return self._parse_response(response, RemoveAPIKeysResponse)

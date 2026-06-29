from __future__ import annotations

from ..enums.api_key import APIKeyStatus
from ._base import List, Optional, PasarguardModel, datetime
from .admin_role import RolePermissions


class APIKeyCreate(PasarguardModel):
    name: str = ...
    note: Optional[str] = None
    permissions: Optional[RolePermissions] = None
    inherit_permissions: Optional[bool] = True
    expire_date: Optional[datetime] = None
    admin_id: Optional[int] = None


class APIKeyCreateResponse(PasarguardModel):
    name: str = ...
    note: Optional[str] = None
    permissions: Optional[RolePermissions] = None
    inherit_permissions: Optional[bool] = True
    expire_date: Optional[datetime] = None
    id: int = ...
    admin_id: int = ...
    created_at: datetime = ...
    api_key_trimmed: str = ...
    revoked_at: Optional[datetime] = None
    status: Optional[APIKeyStatus] = APIKeyStatus.ACTIVE
    is_expired: Optional[bool] = False
    api_key: str = ...


class APIKeyResponse(PasarguardModel):
    name: str = ...
    note: Optional[str] = None
    permissions: Optional[RolePermissions] = None
    inherit_permissions: Optional[bool] = True
    expire_date: Optional[datetime] = None
    id: int = ...
    admin_id: int = ...
    created_at: datetime = ...
    api_key_trimmed: str = ...
    revoked_at: Optional[datetime] = None
    status: Optional[APIKeyStatus] = APIKeyStatus.ACTIVE
    is_expired: Optional[bool] = False


class APIKeyUpdate(PasarguardModel):
    admin_id: Optional[int] = None
    name: Optional[str] = None
    note: Optional[str] = None
    permissions: Optional[RolePermissions] = None
    inherit_permissions: Optional[bool] = None
    expire_date: Optional[datetime] = None
    status: Optional[APIKeyStatus] = None


class APIKeysResponse(PasarguardModel):
    api_keys: List[APIKeyResponse] = ...
    total: int = ...


class BulkAPIKeySelection(PasarguardModel):
    ids: Optional[List[int]] = None


class RemoveAPIKeysResponse(PasarguardModel):
    api_keys: List[str] = ...
    count: int = ...


__all__ = (
    "APIKeyCreate",
    "APIKeyCreateResponse",
    "APIKeyResponse",
    "APIKeyUpdate",
    "APIKeysResponse",
    "BulkAPIKeySelection",
    "RemoveAPIKeysResponse",
)

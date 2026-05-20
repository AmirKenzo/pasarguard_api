from __future__ import annotations

from typing import Any

from pydantic import model_serializer, model_validator

from ._base import List, Optional, PasarguardModel, Union, datetime
from ..enums.admin import PermissionScope


class CRUDPermissions(PasarguardModel):
    create: Optional[bool] = None
    read: Optional[bool] = None
    read_simple: Optional[bool] = None
    update: Optional[bool] = None
    delete: Optional[bool] = None


class AdminsPermissions(PasarguardModel):
    create: Optional[bool] = None
    read: Optional[bool] = None
    read_simple: Optional[bool] = None
    update: Optional[bool] = None
    delete: Optional[bool] = None
    reset_usage: Optional[bool] = None


class NodesPermissions(PasarguardModel):
    create: Optional[bool] = None
    read: Optional[bool] = None
    read_simple: Optional[bool] = None
    update: Optional[bool] = None
    delete: Optional[bool] = None
    reconnect: Optional[bool] = None
    update_core: Optional[bool] = None
    logs: Optional[bool] = None
    stats: Optional[bool] = None


class HostsPermissions(PasarguardModel):
    create: Optional[bool] = None
    read: Optional[bool] = None
    update: Optional[bool] = None


class HwidsPermissions(PasarguardModel):
    read: Optional[bool] = None
    delete: Optional[bool] = None


class SettingsPermissions(PasarguardModel):
    read: Optional[bool] = None
    read_general: Optional[bool] = None
    update: Optional[bool] = None


class SystemPermissions(PasarguardModel):
    read: Optional[bool] = None


class UsersPermissions(PasarguardModel):
    create: Optional[Union[bool, PermissionScope]] = None
    read: Optional[Union[bool, PermissionScope]] = None
    read_simple: Optional[Union[bool, PermissionScope]] = None
    update: Optional[Union[bool, PermissionScope]] = None
    delete: Optional[Union[bool, PermissionScope]] = None
    reset_usage: Optional[Union[bool, PermissionScope]] = None
    revoke_sub: Optional[Union[bool, PermissionScope]] = None
    set_owner: Optional[Union[bool, PermissionScope]] = None
    activate_next_plan: Optional[Union[bool, PermissionScope]] = None

    @model_validator(mode="before")
    @classmethod
    def _parse_api_payload(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data
        return {key: cls._parse_value(value) for key, value in data.items()}

    @staticmethod
    def _parse_value(value: Any) -> Union[bool, PermissionScope, None]:
        if value is None:
            return None
        if isinstance(value, bool):
            return value
        if isinstance(value, PermissionScope):
            return value
        if isinstance(value, int):
            return PermissionScope(value)
        if isinstance(value, dict):
            return PermissionScope(int(value["scope"]))
        raise ValueError(f"invalid user permission: {value!r}")

    @staticmethod
    def _wire_value(value: Union[bool, PermissionScope, int, None]) -> Any:
        if value is None:
            return None
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            value = PermissionScope(value)
        if value is PermissionScope.NONE:
            return None
        return {"scope": int(value)}

    @model_serializer(mode="wrap")
    def _to_api_payload(self, handler):
        return {
            key: wired
            for key, value in handler(self).items()
            if (wired := self._wire_value(value)) is not None
        }


class RoleLimits(PasarguardModel):
    max_users: Optional[int] = None
    data_limit_min: Optional[int] = None
    data_limit_max: Optional[int] = None
    expire_min: Optional[int] = None
    expire_max: Optional[int] = None
    min_hwid_per_user: Optional[int] = None
    max_hwid_per_user: Optional[int] = None


class RoleFeatures(PasarguardModel):
    can_use_reset_strategy: Optional[bool] = True
    can_use_next_plan: Optional[bool] = True


class RoleAccess(PasarguardModel):
    require_template: Optional[bool] = False
    allowed_template_ids: Optional[List[int]] = None
    allowed_group_ids: Optional[List[int]] = None


class RolePermissions(PasarguardModel):
    users: Optional[UsersPermissions] = None
    admins: Optional[AdminsPermissions] = None
    nodes: Optional[NodesPermissions] = None
    groups: Optional[CRUDPermissions] = None
    hosts: Optional[HostsPermissions] = None
    templates: Optional[CRUDPermissions] = None
    client_templates: Optional[CRUDPermissions] = None
    cores: Optional[CRUDPermissions] = None
    settings: Optional[SettingsPermissions] = None
    system: Optional[SystemPermissions] = None
    hwids: Optional[HwidsPermissions] = None
    admin_roles: Optional[CRUDPermissions] = None


class AdminRoleCreate(PasarguardModel):
    name: str = ...
    permissions: Optional[RolePermissions] = None
    limits: Optional[RoleLimits] = None
    features: Optional[RoleFeatures] = None
    access: Optional[RoleAccess] = None
    disabled_when_limited: Optional[bool] = False
    disable_users_when_limited: Optional[bool] = True


class AdminRoleData(PasarguardModel):
    id: Optional[int] = None
    name: Optional[str] = ""
    is_owner: Optional[bool] = False
    permissions: Optional[RolePermissions] = None
    limits: Optional[RoleLimits] = None
    features: Optional[RoleFeatures] = None
    access: Optional[RoleAccess] = None
    disabled_when_limited: Optional[bool] = False
    disable_users_when_limited: Optional[bool] = True


class AdminRoleModify(PasarguardModel):
    name: Optional[str] = None
    permissions: Optional[RolePermissions] = None
    limits: Optional[RoleLimits] = None
    features: Optional[RoleFeatures] = None
    access: Optional[RoleAccess] = None
    disabled_when_limited: Optional[bool] = None
    disable_users_when_limited: Optional[bool] = None


class AdminRoleResponse(PasarguardModel):
    name: str = ...
    permissions: Optional[RolePermissions] = None
    limits: Optional[RoleLimits] = None
    features: Optional[RoleFeatures] = None
    access: Optional[RoleAccess] = None
    disabled_when_limited: Optional[bool] = False
    disable_users_when_limited: Optional[bool] = True
    id: int = ...
    is_owner: bool = ...
    created_at: datetime = ...


class AdminRoleSimple(PasarguardModel):
    id: int = ...
    name: str = ...
    is_owner: bool = ...


class AdminRolesResponse(PasarguardModel):
    roles: List[AdminRoleResponse] = ...
    total: int = ...


class AdminRolesSimpleResponse(PasarguardModel):
    roles: List[AdminRoleSimple] = ...
    total: int = ...


class OwnerCreateRequest(PasarguardModel):
    key: str = ...
    username: str = ...
    password: str = ...


class OwnerDeleteRequest(PasarguardModel):
    key: str = ...


class OwnerResetRequest(PasarguardModel):
    key: str = ...
    password: str = ...


__all__ = (
    "CRUDPermissions",
    "AdminsPermissions",
    "NodesPermissions",
    "HostsPermissions",
    "HwidsPermissions",
    "SettingsPermissions",
    "SystemPermissions",
    "UsersPermissions",
    "RoleLimits",
    "RoleFeatures",
    "RoleAccess",
    "RolePermissions",
    "AdminRoleCreate",
    "AdminRoleData",
    "AdminRoleModify",
    "AdminRoleResponse",
    "AdminRoleSimple",
    "AdminRolesResponse",
    "AdminRolesSimpleResponse",
    "OwnerCreateRequest",
    "OwnerDeleteRequest",
    "OwnerResetRequest",
)

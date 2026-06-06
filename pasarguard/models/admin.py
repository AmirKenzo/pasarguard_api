from __future__ import annotations

from ._base import List, Optional, PasarguardModel
from ..enums.admin import AdminAccountStatus, AdminStatus
from .admin_role import AdminRoleData, RoleLimits

class AdminBase(PasarguardModel):
    id: Optional[int] = None
    username: str = ...

class AdminContactInfo(PasarguardModel):
    id: Optional[int] = None
    username: str = ...
    telegram_id: Optional[int] = None
    discord_webhook: Optional[str] = None
    sub_domain: Optional[str] = None
    profile_title: Optional[str] = None
    support_url: Optional[str] = None
    notification_enable: Optional[AdminNotificationEnable] = None

class AdminCreate(PasarguardModel):
    password: str = ...
    role_id: int = ...
    username: str = ...
    telegram_id: Optional[int] = None
    discord_webhook: Optional[str] = None
    status: Optional[AdminAccountStatus] = None
    data_limit: Optional[int] = None
    sub_template: Optional[str] = None
    sub_domain: Optional[str] = None
    profile_title: Optional[str] = None
    support_url: Optional[str] = None
    note: Optional[str] = None
    notification_enable: Optional[AdminNotificationEnable] = None
    permission_overrides: Optional[RoleLimits] = None

class AdminDetails(PasarguardModel):
    username: str = ...
    is_disabled: bool = ...
    is_limited: bool = ...
    telegram_id: Optional[int] = None
    discord_webhook: Optional[str] = None
    sub_domain: Optional[str] = None
    profile_title: Optional[str] = None
    support_url: Optional[str] = None
    notification_enable: Optional[AdminNotificationEnable] = None
    id: Optional[int] = None
    total_users: Optional[int] = 0
    used_traffic: Optional[int] = 0
    data_limit: Optional[int] = None
    status: Optional[AdminStatus] = AdminStatus.ACTIVE
    sub_template: Optional[str] = None
    lifetime_used_traffic: Optional[int] = None
    note: Optional[str] = None
    role: Optional[AdminRoleData] = None
    permission_overrides: Optional[RoleLimits] = None

class AdminModify(PasarguardModel):
    password: Optional[str] = None
    telegram_id: Optional[int] = None
    discord_webhook: Optional[str] = None
    status: Optional[AdminAccountStatus] = None
    data_limit: Optional[int] = None
    sub_template: Optional[str] = None
    sub_domain: Optional[str] = None
    profile_title: Optional[str] = None
    support_url: Optional[str] = None
    note: Optional[str] = None
    notification_enable: Optional[AdminNotificationEnable] = None
    role_id: Optional[int] = None
    permission_overrides: Optional[RoleLimits] = None

class AdminNotificationEnable(PasarguardModel):
    create: Optional[bool] = True
    modify: Optional[bool] = True
    delete: Optional[bool] = True
    reset_usage: Optional[bool] = True
    login: Optional[bool] = True
    usage_limit_warning: Optional[bool] = True
    usage_limit_warning_percentages: Optional[List[int]] = None

class AdminSimple(PasarguardModel):
    id: int = ...
    username: str = ...

class AdminsResponse(PasarguardModel):
    admins: List[AdminDetails] = ...
    total: int = ...
    active: int = ...
    disabled: int = ...
    limited: int = ...

class AdminsSimpleResponse(PasarguardModel):
    admins: List[AdminSimple] = ...
    total: int = ...

class BodyAdminTokenApiAdminTokenPost(PasarguardModel):
    grant_type: Optional[str] = None
    username: str = ...
    password: str = ...
    scope: Optional[str] = ''
    client_id: Optional[str] = None
    client_secret: Optional[str] = None

class BulkAdminSelection(PasarguardModel):
    ids: Optional[List[int]] = None

class BulkAdminsActionResponse(PasarguardModel):
    admins: List[str] = ...
    count: int = ...

class RemoveAdminsResponse(PasarguardModel):
    admins: List[str] = ...
    count: int = ...

class Token(PasarguardModel):
    access_token: str = ...
    token_type: Optional[str] = 'bearer'

Admin = AdminDetails

__all__ = (
    'AdminBase',
    'AdminContactInfo',
    'AdminCreate',
    'AdminDetails',
    'AdminModify',
    'AdminNotificationEnable',
    'AdminSimple',
    'AdminsResponse',
    'AdminsSimpleResponse',
    'BodyAdminTokenApiAdminTokenPost',
    'BulkAdminSelection',
    'BulkAdminsActionResponse',
    'RemoveAdminsResponse',
    'Token',
    'Admin',
)

from __future__ import annotations

# ruff: noqa: F401, F403
from ._base import *

class AdminBase(PasarguardModel):
    username: str = ...

class AdminContactInfo(PasarguardModel):
    username: str = ...
    telegram_id: Optional[int] = None
    discord_webhook: Optional[str] = None
    sub_domain: Optional[str] = None
    profile_title: Optional[str] = None
    support_url: Optional[str] = None
    notification_enable: Optional[UserNotificationEnable] = None

class AdminCreate(PasarguardModel):
    password: str = ...
    is_sudo: bool = ...
    telegram_id: Optional[int] = None
    discord_webhook: Optional[str] = None
    discord_id: Optional[int] = None
    is_disabled: Optional[bool] = None
    sub_template: Optional[str] = None
    sub_domain: Optional[str] = None
    profile_title: Optional[str] = None
    support_url: Optional[str] = None
    note: Optional[str] = None
    notification_enable: Optional[UserNotificationEnable] = None
    username: str = ...

class AdminDetails(PasarguardModel):
    username: str = ...
    telegram_id: Optional[int] = None
    discord_webhook: Optional[str] = None
    sub_domain: Optional[str] = None
    profile_title: Optional[str] = None
    support_url: Optional[str] = None
    notification_enable: Optional[UserNotificationEnable] = None
    id: Optional[int] = None
    is_sudo: bool = ...
    total_users: Optional[int] = 0
    used_traffic: Optional[int] = 0
    is_disabled: Optional[bool] = False
    discord_id: Optional[int] = None
    sub_template: Optional[str] = None
    lifetime_used_traffic: Optional[int] = None
    note: Optional[str] = None

class AdminModify(PasarguardModel):
    password: Optional[str] = None
    is_sudo: bool = ...
    telegram_id: Optional[int] = None
    discord_webhook: Optional[str] = None
    discord_id: Optional[int] = None
    is_disabled: Optional[bool] = None
    sub_template: Optional[str] = None
    sub_domain: Optional[str] = None
    profile_title: Optional[str] = None
    support_url: Optional[str] = None
    note: Optional[str] = None
    notification_enable: Optional[UserNotificationEnable] = None

class AdminNotificationEnable(PasarguardModel):
    create: Optional[bool] = True
    modify: Optional[bool] = True
    delete: Optional[bool] = True
    reset_usage: Optional[bool] = True
    login: Optional[bool] = True

class AdminSimple(PasarguardModel):
    id: int = ...
    username: str = ...

class AdminsResponse(PasarguardModel):
    admins: List[AdminDetails] = ...
    total: int = ...
    active: int = ...
    disabled: int = ...

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
    usernames: Optional[List[str]] = None

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

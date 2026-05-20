from __future__ import annotations

from ._base import DataLimitResetStrategy, List, Optional, PasarguardModel, UserStatusCreate
from .proxy import ExtraSettings

class BulkUserTemplateSelection(PasarguardModel):
    ids: Optional[List[int]] = None

class BulkUserTemplatesActionResponse(PasarguardModel):
    templates: List[str] = ...
    count: int = ...

class RemoveUserTemplatesResponse(PasarguardModel):
    templates: List[str] = ...
    count: int = ...

class UserTemplateCreate(PasarguardModel):
    name: Optional[str] = None
    data_limit: Optional[int] = None
    hwid_limit: Optional[int] = None
    expire_duration: Optional[int] = None
    username_prefix: Optional[str] = None
    username_suffix: Optional[str] = None
    group_ids: List[int] = ...
    extra_settings: Optional[ExtraSettings] = None
    status: Optional[UserStatusCreate] = None
    reset_usages: Optional[bool] = None
    on_hold_timeout: Optional[int] = None
    data_limit_reset_strategy: Optional[DataLimitResetStrategy] = 'no_reset'
    is_disabled: Optional[bool] = None

class UserTemplateModify(PasarguardModel):
    name: Optional[str] = None
    data_limit: Optional[int] = None
    hwid_limit: Optional[int] = None
    expire_duration: Optional[int] = None
    username_prefix: Optional[str] = None
    username_suffix: Optional[str] = None
    group_ids: Optional[List[int]] = None
    extra_settings: Optional[ExtraSettings] = None
    status: Optional[UserStatusCreate] = None
    reset_usages: Optional[bool] = None
    on_hold_timeout: Optional[int] = None
    data_limit_reset_strategy: Optional[DataLimitResetStrategy] = 'no_reset'
    is_disabled: Optional[bool] = None

class UserTemplateResponse(PasarguardModel):
    name: Optional[str] = None
    data_limit: Optional[int] = None
    hwid_limit: Optional[int] = None
    expire_duration: Optional[int] = None
    username_prefix: Optional[str] = None
    username_suffix: Optional[str] = None
    group_ids: List[int] = ...
    extra_settings: Optional[ExtraSettings] = None
    status: Optional[UserStatusCreate] = None
    reset_usages: Optional[bool] = None
    on_hold_timeout: Optional[int] = None
    data_limit_reset_strategy: Optional[DataLimitResetStrategy] = 'no_reset'
    is_disabled: Optional[bool] = None
    id: int = ...

class UserTemplateSimple(PasarguardModel):
    id: int = ...
    name: Optional[str] = None

class UserTemplatesSimpleResponse(PasarguardModel):
    templates: List[UserTemplateSimple] = ...
    total: int = ...

__all__ = (
    'BulkUserTemplateSelection',
    'BulkUserTemplatesActionResponse',
    'RemoveUserTemplatesResponse',
    'UserTemplateCreate',
    'UserTemplateModify',
    'UserTemplateResponse',
    'UserTemplateSimple',
    'UserTemplatesSimpleResponse',
)

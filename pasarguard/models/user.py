from __future__ import annotations

from ._base import (
    DataLimitResetStrategy,
    Dict,
    List,
    Optional,
    PasarguardModel,
    Period,
    ShadowsocksMethods,
    Union,
    UserCountMetric,
    UsernameGenerationStrategy,
    UserStatus,
    datetime,
)
from .admin import AdminBase
from .proxy import ProxyTable


class BulkUser(PasarguardModel):
    dry_run: Optional[bool] = False
    group_ids: Optional[List[int]] = None
    admins: Optional[List[int]] = None
    users: Optional[List[int]] = None
    status: Optional[List[UserStatus]] = None
    expire_after: Optional[datetime] = None
    expire_before: Optional[datetime] = None
    amount: int = ...


class BulkUsersActionResponse(PasarguardModel):
    users: List[str] = ...
    count: int = ...


class BulkUsersApplyTemplate(PasarguardModel):
    user_template_id: int = ...
    note: Optional[str] = None
    ids: Optional[List[int]] = None


class BulkUsersCreateResponse(PasarguardModel):
    subscription_urls: Optional[List[str]] = None
    created: Optional[int] = 0


class BulkUsersFromTemplate(PasarguardModel):
    user_template_id: int = ...
    note: Optional[str] = None
    username: Optional[str] = None
    count: int = ...
    strategy: Optional[UsernameGenerationStrategy] = "random"
    start_number: Optional[int] = None


class BulkUsersProxy(PasarguardModel):
    dry_run: Optional[bool] = False
    group_ids: Optional[List[int]] = None
    admins: Optional[List[int]] = None
    users: Optional[List[int]] = None
    status: Optional[List[UserStatus]] = None
    expire_after: Optional[datetime] = None
    expire_before: Optional[datetime] = None
    method: Optional[ShadowsocksMethods] = None


class BulkUsersSelection(PasarguardModel):
    ids: Optional[List[int]] = None


class BulkUsersSetOwner(PasarguardModel):
    ids: Optional[List[int]] = None
    admin_username: str = ...


class BulkWireGuardPeerIPs(PasarguardModel):
    dry_run: Optional[bool] = False
    group_ids: Optional[List[int]] = None
    admins: Optional[List[int]] = None
    users: Optional[List[int]] = None
    status: Optional[List[UserStatus]] = None
    expire_after: Optional[datetime] = None
    expire_before: Optional[datetime] = None
    confirm: Optional[bool] = False
    replace_all: Optional[bool] = False


class CreateUserFromTemplate(PasarguardModel):
    user_template_id: int = ...
    note: Optional[str] = None
    username: str = ...


class ModifyUserByTemplate(PasarguardModel):
    user_template_id: int = ...
    note: Optional[str] = None


class NextPlanModel(PasarguardModel):
    user_template_id: Optional[int] = None
    data_limit: Optional[int] = None
    expire: Optional[int] = None
    add_remaining_traffic: Optional[bool] = False


class RemoveUsersResponse(PasarguardModel):
    users: List[str] = ...
    count: int = ...


class UserCountMetricStat(PasarguardModel):
    count: int = ...
    period_start: datetime = ...


class UserCountMetricStatsList(PasarguardModel):
    period: Optional[Period] = None
    start: datetime = ...
    end: datetime = ...
    metric: UserCountMetric = ...
    stats: Dict[str, List[UserCountMetricStat]] = ...
    count_during_period: Optional[int] = None


class UserCreate(PasarguardModel):
    proxy_settings: Optional[ProxyTable] = None
    expire: Optional[Union[datetime, int]] = None
    data_limit: Optional[int] = None
    data_limit_reset_strategy: Optional[DataLimitResetStrategy] = None
    note: Optional[str] = None
    on_hold_expire_duration: Optional[int] = None
    on_hold_timeout: Optional[Union[datetime, int]] = None
    group_ids: Optional[List[int]] = None
    auto_delete_in_days: Optional[int] = None
    hwid_limit: Optional[int] = None
    next_plan: Optional[NextPlanModel] = None
    username: str = ...
    status: Optional[UserStatus] = None


class UserModify(PasarguardModel):
    proxy_settings: Optional[ProxyTable] = None
    expire: Optional[Union[datetime, int]] = None
    data_limit: Optional[int] = None
    data_limit_reset_strategy: Optional[DataLimitResetStrategy] = None
    note: Optional[str] = None
    on_hold_expire_duration: Optional[int] = None
    on_hold_timeout: Optional[Union[datetime, int]] = None
    group_ids: Optional[List[int]] = None
    auto_delete_in_days: Optional[int] = None
    hwid_limit: Optional[int] = None
    next_plan: Optional[NextPlanModel] = None
    status: Optional[UserStatus] = None


class UserNotificationEnable(PasarguardModel):
    create: Optional[bool] = True
    modify: Optional[bool] = True
    delete: Optional[bool] = True
    status_change: Optional[bool] = True
    reset_data_usage: Optional[bool] = True
    data_reset_by_next: Optional[bool] = True
    subscription_revoked: Optional[bool] = True


class UserResponse(PasarguardModel):
    proxy_settings: Optional[ProxyTable] = None
    expire: Optional[Union[datetime, int]] = None
    data_limit: Optional[int] = None
    data_limit_reset_strategy: Optional[DataLimitResetStrategy] = None
    note: Optional[str] = None
    on_hold_expire_duration: Optional[int] = None
    on_hold_timeout: Optional[Union[datetime, int]] = None
    group_ids: Optional[List[int]] = None
    auto_delete_in_days: Optional[int] = None
    hwid_limit: Optional[int] = None
    next_plan: Optional[NextPlanModel] = None
    id: int = ...
    username: str = ...
    status: UserStatus = ...
    used_traffic: int = ...
    lifetime_used_traffic: Optional[int] = 0
    created_at: datetime = ...
    edit_at: Optional[datetime] = None
    online_at: Optional[datetime] = None
    subscription_url: Optional[str] = ""
    admin: Optional[AdminBase] = None


class UserSimple(PasarguardModel):
    id: int = ...
    username: str = ...


class UserSubscriptionUpdateChart(PasarguardModel):
    total: int = ...
    segments: Optional[List[UserSubscriptionUpdateChartSegment]] = None


class UserSubscriptionUpdateChartSegment(PasarguardModel):
    name: str = ...
    count: int = ...
    percentage: float = ...


class UserSubscriptionUpdateList(PasarguardModel):
    updates: Optional[List[UserSubscriptionUpdateSchema]] = None
    count: int = ...


class UserSubscriptionUpdateSchema(PasarguardModel):
    created_at: datetime = ...
    user_agent: str = ...
    ip: Optional[str] = None
    hwid: Optional[str] = None


class UserUsageStat(PasarguardModel):
    total_traffic: int = ...
    period_start: datetime = ...


class UserUsageStatsList(PasarguardModel):
    period: Optional[Period] = None
    start: datetime = ...
    end: datetime = ...
    stats: Dict[str, List[UserUsageStat]] = ...


class UsersResponse(PasarguardModel):
    users: List[UserResponse] = ...
    total: int = ...


class UsersSimpleResponse(PasarguardModel):
    users: List[UserSimple] = ...
    total: int = ...


class UserStatusToggle(PasarguardModel):
    disabled: bool = ...


class WireGuardPeerIPsReallocateResponse(PasarguardModel):
    wireguard_inbound_tags: int = ...
    candidates: int = ...
    updated: int = ...
    dry_run: bool = ...
    sample_usernames: List[str] = ...
    affected_users: int = ...


__all__ = (
    "BulkUser",
    "BulkUsersActionResponse",
    "BulkUsersApplyTemplate",
    "BulkUsersCreateResponse",
    "BulkUsersFromTemplate",
    "BulkUsersProxy",
    "BulkUsersSelection",
    "BulkUsersSetOwner",
    "BulkWireGuardPeerIPs",
    "CreateUserFromTemplate",
    "ModifyUserByTemplate",
    "NextPlanModel",
    "RemoveUsersResponse",
    "UserCountMetricStat",
    "UserCountMetricStatsList",
    "UserCreate",
    "UserModify",
    "UserNotificationEnable",
    "UserResponse",
    "UserSimple",
    "UserStatusToggle",
    "UserSubscriptionUpdateChart",
    "UserSubscriptionUpdateChartSegment",
    "UserSubscriptionUpdateList",
    "UserSubscriptionUpdateSchema",
    "UserUsageStat",
    "UserUsageStatsList",
    "UsersResponse",
    "UsersSimpleResponse",
    "WireGuardPeerIPsReallocateResponse",
)

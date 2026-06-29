from __future__ import annotations

from ._base import (
    Any,
    ConfigFormat,
    DataLimitResetStrategy,
    Dict,
    Language,
    List,
    Optional,
    PasarguardModel,
    Platform,
    Union,
    UserStatus,
    datetime,
)
from .common import CustomVariable
from .proxy import ProxyTable
from .user import NextPlanModel


class Application(PasarguardModel):
    name: str = ...
    icon_url: Optional[str] = ""
    import_url: Optional[str] = ""
    description: Optional[Dict[str, str]] = None
    recommended: Optional[bool] = False
    show_when_hwid_enabled: Optional[bool] = False
    platform: Platform = ...
    download_links: List[DownloadLink] = ...


class DownloadLink(PasarguardModel):
    name: str = ...
    url: str = ...
    language: Language = ...


class SubFormatEnable(PasarguardModel):
    links: Optional[bool] = True
    links_base64: Optional[bool] = True
    xray: Optional[bool] = True
    wireguard: Optional[bool] = True
    sing_box: Optional[bool] = True
    clash: Optional[bool] = True
    clash_meta: Optional[bool] = True
    outline: Optional[bool] = True


class SubRule(PasarguardModel):
    pattern: str = ...
    target: ConfigFormat = ...
    response_headers: Optional[Dict[str, Any]] = None


class Subscription(PasarguardModel):
    url_prefix: Optional[str] = ""
    update_interval: Optional[int] = 12
    support_url: Optional[str] = "https://t.me/"
    profile_title: Optional[str] = "Subscription"
    announce: Optional[str] = ""
    announce_url: Optional[str] = ""
    response_headers: Optional[Dict[str, Any]] = None
    rules: List[SubRule] = ...
    manual_sub_request: Optional[SubFormatEnable] = None
    applications: Optional[List[Application]] = None
    allow_browser_config: Optional[bool] = True
    disable_sub_template: Optional[bool] = False
    randomize_order: Optional[bool] = False
    custom_variables: Optional[List[CustomVariable]] = None


class SubscriptionTemplates(PasarguardModel):
    xray: Optional[int] = None


class SubscriptionUserResponse(PasarguardModel):
    proxy_settings: Optional[ProxyTable] = None
    expire: Optional[Union[datetime, int]] = None
    data_limit: Optional[int] = None
    data_limit_reset_strategy: Optional[DataLimitResetStrategy] = None
    on_hold_expire_duration: Optional[int] = None
    on_hold_timeout: Optional[Union[datetime, int]] = None
    group_ids: Optional[List[int]] = None
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
    ip: Optional[str] = None


__all__ = (
    "Application",
    "DownloadLink",
    "SubFormatEnable",
    "SubRule",
    "Subscription",
    "SubscriptionTemplates",
    "SubscriptionUserResponse",
)

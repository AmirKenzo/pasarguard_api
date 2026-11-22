from __future__ import annotations

from ._base import (
    Field,
    HWIDMode,
    List,
    OnHoldTimeoutAction,
    Optional,
    PasarguardModel,
    RunMethod,
    ShadowsocksMethods,
)
from .admin import AdminNotificationEnable
from .common import BaseNotificationEnable, CustomVariable
from .host import HostNotificationEnable
from .node import NodeNotificationEnable
from .subscription import Subscription
from .user import UserNotificationEnable


class UsageSettings(PasarguardModel):
    record_node_usage: Optional[bool] = True
    record_node_stats: Optional[bool] = False
    reset_usage_clean_chart_data: Optional[bool] = False
    record_outbound_usage: Optional[bool] = False


class NodeHealthSettings(PasarguardModel):
    fail_threshold: Optional[int] = 3
    recover_threshold: Optional[int] = 2
    probe_timeout: Optional[int] = 5
    max_backoff: Optional[int] = 60


class CleanupSettings(PasarguardModel):
    expired_users_retention_days: Optional[int] = None
    include_limited_users: Optional[bool] = False
    usage_history_retention_days: Optional[int] = None
    node_stats_retention_days: Optional[int] = None
    usage_rollup_hourly_after_days: Optional[int] = None
    usage_rollup_half_day_after_days: Optional[int] = None
    usage_rollup_daily_after_days: Optional[int] = None


class General(PasarguardModel):
    default_method: Optional[ShadowsocksMethods] = "chacha20-ietf-poly1305"
    on_hold_timeout_action: Optional[OnHoldTimeoutAction] = OnHoldTimeoutAction.ACTIVATE
    custom_variables: Optional[List[CustomVariable]] = None
    usage: Optional[UsageSettings] = None
    node_health: Optional[NodeHealthSettings] = None
    stop_nodes_on_shutdown: Optional[bool] = True


class HWIDSettings(PasarguardModel):
    enabled: Optional[bool] = True
    forced: Optional[bool] = False
    require_hwid_for_manual_sub: Optional[bool] = False
    fallback_limit: Optional[int] = None
    min_limit: Optional[int] = None
    max_limit: Optional[int] = None


class RoleHWIDSettings(PasarguardModel):
    enabled: Optional[bool] = True
    forced: Optional[bool] = False
    require_hwid_for_manual_sub: Optional[bool] = False
    fallback_limit: Optional[int] = None
    min_limit: Optional[int] = None
    max_limit: Optional[int] = None
    mode: Optional[HWIDMode] = HWIDMode.USE_GLOBAL


class NotificationChannel(PasarguardModel):
    telegram_chat_id: Optional[int] = None
    telegram_topic_id: Optional[int] = None
    discord_webhook_url: Optional[str] = None


class NotificationChannels(PasarguardModel):
    admin: Optional[NotificationChannel] = None
    admin_role: Optional[NotificationChannel] = None
    core: Optional[NotificationChannel] = None
    group: Optional[NotificationChannel] = None
    host: Optional[NotificationChannel] = None
    node: Optional[NotificationChannel] = None
    user: Optional[NotificationChannel] = None
    user_template: Optional[NotificationChannel] = None
    api_key: Optional[NotificationChannel] = None


class NotificationEnable(PasarguardModel):
    admin: Optional[AdminNotificationEnable] = None
    admin_role: Optional[BaseNotificationEnable] = None
    core: Optional[BaseNotificationEnable] = None
    group: Optional[BaseNotificationEnable] = None
    host: Optional[HostNotificationEnable] = None
    node: Optional[NodeNotificationEnable] = None
    user: Optional[UserNotificationEnable] = None
    user_template: Optional[BaseNotificationEnable] = None
    api_key: Optional[BaseNotificationEnable] = None
    days_left: Optional[bool] = True
    percentage_reached: Optional[bool] = True


class NotificationSettings(PasarguardModel):
    notify_telegram: Optional[bool] = False
    notify_discord: Optional[bool] = False
    telegram_api_token: Optional[str] = None
    telegram_chat_id: Optional[int] = None
    telegram_topic_id: Optional[int] = None
    discord_webhook_url: Optional[str] = None
    channels: Optional[NotificationChannels] = None
    proxy_url: Optional[str] = None
    max_retries: int = ...


class SettingsSchema(PasarguardModel):
    telegram: Optional[Telegram] = None
    webhook: Optional[Webhook] = None
    notification_settings: Optional[NotificationSettings] = None
    notification_enable: Optional[NotificationEnable] = None
    subscription: Optional[Subscription] = None
    hwid: Optional[HWIDSettings] = None
    general: Optional[General] = None
    cleanup: Optional[CleanupSettings] = None


class Telegram(PasarguardModel):
    enable: Optional[bool] = False
    token: Optional[str] = None
    webhook_url: Optional[str] = None
    webhook_secret: Optional[str] = None
    proxy_url: Optional[str] = None
    method: Optional[RunMethod] = "webhook"
    mini_app_login: Optional[bool] = True
    mini_app_web_url: Optional[str] = ""
    for_admins_only: Optional[bool] = True


class Webhook(PasarguardModel):
    enable: Optional[bool] = False
    webhooks: Optional[List[WebhookInfo]] = Field(default_factory=list)
    days_left: Optional[List[int]] = Field(default_factory=list)
    usage_percent: Optional[List[int]] = Field(default_factory=list)
    timeout: int = ...
    recurrent: int = ...
    proxy_url: Optional[str] = None


class WebhookInfo(PasarguardModel):
    url: str = ...
    secret: str = ...


__all__ = (
    "CleanupSettings",
    "General",
    "HWIDSettings",
    "NodeHealthSettings",
    "NotificationChannel",
    "NotificationChannels",
    "NotificationEnable",
    "NotificationSettings",
    "RoleHWIDSettings",
    "SettingsSchema",
    "Telegram",
    "UsageSettings",
    "Webhook",
    "WebhookInfo",
)

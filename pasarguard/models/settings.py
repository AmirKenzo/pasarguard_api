from __future__ import annotations

from ._base import HWIDMode, List, Optional, PasarguardModel, RunMethod, ShadowsocksMethods
from .admin import AdminNotificationEnable
from .common import BaseNotificationEnable
from .host import HostNotificationEnable
from .node import NodeNotificationEnable
from .subscription import Subscription
from .user import UserNotificationEnable

class General(PasarguardModel):
    default_method: Optional[ShadowsocksMethods] = 'chacha20-ietf-poly1305'

class HWIDSettings(PasarguardModel):
    enabled: Optional[bool] = False
    forced: Optional[bool] = False
    require_hwid_for_manual_sub: Optional[bool] = True
    fallback_limit: Optional[int] = 0
    min_limit: Optional[int] = 0
    max_limit: Optional[int] = 0

class RoleHWIDSettings(PasarguardModel):
    enabled: Optional[bool] = True
    forced: Optional[bool] = False
    require_hwid_for_manual_sub: Optional[bool] = True
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

class NotificationEnable(PasarguardModel):
    admin: Optional[AdminNotificationEnable] = None
    admin_role: Optional[BaseNotificationEnable] = None
    core: Optional[BaseNotificationEnable] = None
    group: Optional[BaseNotificationEnable] = None
    host: Optional[HostNotificationEnable] = None
    node: Optional[NodeNotificationEnable] = None
    user: Optional[UserNotificationEnable] = None
    user_template: Optional[BaseNotificationEnable] = None
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

class Telegram(PasarguardModel):
    enable: Optional[bool] = False
    token: Optional[str] = None
    webhook_url: Optional[str] = None
    webhook_secret: Optional[str] = None
    proxy_url: Optional[str] = None
    method: Optional[RunMethod] = 'webhook'
    mini_app_login: Optional[bool] = True
    mini_app_web_url: Optional[str] = ''
    for_admins_only: Optional[bool] = True

class Webhook(PasarguardModel):
    enable: Optional[bool] = False
    webhooks: Optional[List[WebhookInfo]] = []
    days_left: Optional[List[int]] = []
    usage_percent: Optional[List[int]] = []
    timeout: int = ...
    recurrent: int = ...
    proxy_url: Optional[str] = None

class WebhookInfo(PasarguardModel):
    url: str = ...
    secret: str = ...

__all__ = (
    'General',
    'HWIDSettings',
    'RoleHWIDSettings',
    'NotificationChannel',
    'NotificationChannels',
    'NotificationEnable',
    'NotificationSettings',
    'SettingsSchema',
    'Telegram',
    'Webhook',
    'WebhookInfo',
)

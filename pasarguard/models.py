from datetime import datetime
from typing import Any, ClassVar, Dict, List, Literal, Optional

from pydantic import BaseModel, Field, RootModel, field_validator, ConfigDict

from .enums import FlowOption, ShadowsocksMethod, UserDataLimitResetStrategy


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class NotificationEnable(BaseModel):
    create: Optional[bool] = None
    modify: Optional[bool] = None
    delete: Optional[bool] = None
    status_change: Optional[bool] = None
    reset_data_usage: Optional[bool] = None
    data_reset_by_next: Optional[bool] = None
    subscription_revoked: Optional[bool] = None


class Admin(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    telegram_id: Optional[int] = None
    discord_webhook: Optional[str] = None
    sub_domain: Optional[str] = None
    is_sudo: Optional[bool] = None
    total_users: Optional[int] = None
    used_traffic: Optional[int] = None
    is_disabled: Optional[bool] = None
    discord_id: Optional[int] = None
    sub_template: Optional[str] = None
    profile_title: Optional[str] = None
    support_url: Optional[str] = None
    lifetime_used_traffic: Optional[int] = None
    notification_enable: Optional[NotificationEnable] = None


class AdminCreate(Admin):
    password: str


class AdminModify(BaseModel):
    is_sudo: bool
    password: Optional[str] = None
    telegram_id: Optional[int] = None
    discord_webhook: Optional[str] = None
    users_usage: Optional[int] = None
    is_disabled: Optional[bool] = None


class HTTPValidationError(BaseModel):
    detail: Optional[List[Dict[str, Any]]] = None


# ------------------ VMess ------------------
class VmessSettings(BaseModel):
    id: Optional[str] = None


# ------------------ VLESS ------------------
class VlessSettings(BaseModel):
    id: Optional[str] = None
    flow: Optional[FlowOption] = None


# ------------------ Trojan -----------------
class TrojanSettings(BaseModel):
    password: Optional[str] = Field(default=None, min_length=16)


# ------------------ Shadowsocks ------------
class ShadowsocksSettings(BaseModel):
    password: Optional[str] = Field(default=None, min_length=16)
    method: Optional[ShadowsocksMethod] = None


class ProxySettings(BaseModel):
    vmess: Optional[VmessSettings] = None
    vless: Optional[VlessSettings] = None
    trojan: Optional[TrojanSettings] = None
    shadowsocks: Optional[ShadowsocksSettings] = None


class NextPlanModel(BaseModel):
    add_remaining_traffic: bool = False
    data_limit: Optional[int] = 0
    user_template_id: Optional[int] = 0
    expire: Optional[datetime] = None
    fire_on_either: bool = True

    @field_validator("data_limit", mode="before")
    def validate_data_limit(cls, value):
        if value is not None and value < 0:
            raise ValueError("Data limit in the next plan must be 0 or greater")
        return value


class UserCreate(BaseModel):
    username: str
    proxy_settings: Optional[Dict[str, ProxySettings]] = None
    group_ids: Optional[List[int]] = None
    expire: Optional[datetime] = None
    data_limit: Optional[int] = 0
    data_limit_reset_strategy: UserDataLimitResetStrategy | None = Field(default=None)
    note: Optional[str] = None
    sub_updated_at: Optional[str] = None
    sub_last_user_agent: Optional[str] = None
    online_at: Optional[str] = None
    on_hold_expire_duration: Optional[int] = 0
    on_hold_timeout: Optional[str] = None
    status: Literal["active", "on_hold"] = "active"
    next_plan: Optional[NextPlanModel] = None


class UserResponse(BaseModel):
    username: Optional[str] = None
    proxy_settings: Optional[ProxySettings] = None
    group_ids: Optional[List[int]] = None
    expire: Optional[datetime] = None
    data_limit: Optional[int] = None
    data_limit_reset_strategy: Optional[str] = None
    note: Optional[str] = None
    sub_updated_at: Optional[str] = None
    sub_last_user_agent: Optional[str] = None
    online_at: Optional[str] = None
    on_hold_expire_duration: Optional[int] = None
    id: Optional[int] = None
    on_hold_timeout: Optional[str] = None
    group_ids: Optional[list] = None
    status: Literal["active", "disabled", "limited", "expired", "on_hold"] = "active"
    used_traffic: Optional[int] = None
    lifetime_used_traffic: Optional[int] = None
    subscription_url: Optional[str] = None
    subscription_token: Optional[str] = None
    auto_delete_in_days: Optional[int] = None
    next_plan: Optional[NextPlanModel] = None
    admin: Optional[Admin] = None
    created_at: Optional[str] = None

    def __init__(self, **data):
        super().__init__(**data)
        if not self.subscription_token and self.subscription_url:
            self.subscription_token = self.subscription_url.split("/")[-1]


class NodeCreate(BaseModel):
    name: str
    address: str
    port: int = 62050
    usage_coefficient: float = 1.0
    connection_type: Optional[str] = None
    server_ca: Optional[str] = None
    keep_alive: Optional[int] = None
    core_config_id: Optional[int] = None
    api_key: Optional[str] = None
    api_port: Optional[int] = None


class NodeModify(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    port: Optional[int] = None
    api_port: Optional[int] = None
    usage_coefficient: Optional[float] = None
    status: Optional[str] = None
    connection_type: Optional[str] = None
    server_ca: Optional[str] = None
    keep_alive: Optional[int] = None
    core_config_id: Optional[int] = None
    api_key: Optional[str] = None


class Nodes(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    name: str
    address: str
    port: int
    usage_coefficient: float
    connection_type: str
    server_ca: str
    keep_alive: int
    core_config_id: Optional[int] = None
    api_key: Optional[str] = None
    id: int
    xray_version: Optional[str] = None
    node_version: Optional[str] = None
    status: str
    message: Optional[str] = None
    uplink: Optional[int] = None
    downlink: Optional[int] = None


class NodeResponse(BaseModel):
    nodes: list[Nodes]
    total: int

class NodeUsageResponse(BaseModel):
    node_id: Optional[int] = None
    node_name: Optional[str] = None
    uplink: Optional[int] = None
    downlink: Optional[int] = None


class NodesUsageResponse(BaseModel):
    usages: List[NodeUsageResponse]


class ProxyHost(BaseModel):
    remark: str
    address: str
    port: Optional[int] = None
    sni: Optional[str] = None
    host: Optional[str] = None
    path: Optional[str] = None
    security: str = "inbound_default"
    alpn: str = ""
    fingerprint: str = ""
    allowinsecure: bool
    is_disabled: bool


class HostsModel(RootModel):
    root: Dict[str, List[ProxyHost]]


class ProxyInbound(BaseModel):
    tag: str
    protocol: str
    network: str
    tls: str
    port: Any


class CoreStats(BaseModel):
    version: str
    started: bool
    logs_websocket: str


class UserModify(BaseModel):
    proxy_settings: Optional[ProxySettings] = None
    group_ids: Optional[List[int]] = None
    expire: Optional[datetime] = None
    data_limit: Optional[int] = None
    data_limit_reset_strategy: Optional[Literal["no_reset", "day", "week", "month", "year"]] = None
    note: Optional[str] = None
    sub_updated_at: Optional[str] = None
    sub_last_user_agent: Optional[str] = None
    online_at: Optional[str] = None
    on_hold_expire_duration: Optional[int] = None
    on_hold_timeout: Optional[str] = None
    status: Optional[Literal["active", "disabled", "limited", "expired", "on_hold"]] = None
    next_plan: Optional[NextPlanModel] = None


class UserTemplateCreate(BaseModel):
    name: Optional[str] = None
    group_ids: Optional[List[int]] = []
    data_limit: int = 0
    expire_duration: int = 0
    extra_settings: Optional[ProxySettings] = None
    status: Literal["active", "on_hold"] = "active"
    reset_usages: Optional[bool] = None


class UserTemplateResponse(BaseModel):
    id: int
    name: Optional[str] = None
    group_ids: Optional[List[int]] = None
    data_limit: int
    expire_duration: int
    extra_settings: Optional[ProxySettings] = None
    status: Literal["active", "on_hold"]
    reset_usages: Optional[bool] = None


class UserTemplateModify(BaseModel):
    name: Optional[str] = None
    group_ids: Optional[List[int]] = None
    data_limit: Optional[int] = None
    expire_duration: Optional[int] = None
    extra_settings: Optional[ProxySettings] = None
    status: Optional[Literal["active", "on_hold"]] = None
    reset_usages: Optional[bool] = None


class UserUsageResponse(BaseModel):
    node_id: Optional[int]
    node_name: Optional[str]
    used_traffic: Optional[int]


class UserUsagesResponse(BaseModel):
    username: str
    usages: List[UserUsageResponse]


class UsersResponse(BaseModel):
    users: List[UserResponse]
    total: int


class UserStatus(BaseModel):
    enum: ClassVar[List[str]] = ["active", "disabled", "limited", "expired", "on_hold"]


class ValidationError(BaseModel):
    loc: List[Any]
    msg: str
    type: str


class UserSubscriptionUpdateSchema(BaseModel):
    created_at: datetime | None = Field(default=None)
    user_agent: str | None = Field(default=None)


class UserSubscriptionUpdateList(BaseModel):
    updates: list[UserSubscriptionUpdateSchema] = Field(default_factory=list)
    count: int


class SubscriptionUserResponse(BaseModel):
    proxies: Dict[str, Any]
    expire: Optional[datetime] = None
    data_limit: Optional[int] = None
    data_limit_reset_strategy: str = "no_reset"
    inbounds: Dict[str, List[str]] = {}
    note: Optional[str] = None
    online_at: Optional[str] = None
    on_hold_expire_duration: Optional[int] = None
    on_hold_timeout: Optional[str] = None
    auto_delete_in_days: Optional[int] = None
    username: str
    status: str
    used_traffic: int
    lifetime_used_traffic: int = 0
    created_at: str
    subscription_url: str = ""
    excluded_inbounds: Dict[str, List[str]] = {}
    admin: Optional[Admin] = None


class SystemStats(BaseModel):
    version: Optional[str] = None
    mem_total: Optional[int] = None
    mem_used: Optional[int] = None
    cpu_cores: Optional[int] = None
    cpu_usage: Optional[float] = None
    total_user: Optional[int] = None
    online_users: Optional[int] = None
    active_users: Optional[int] = None
    on_hold_users: Optional[int] = None
    disabled_users: Optional[int] = None
    expired_users: Optional[int] = None
    limited_users: Optional[int] = None
    incoming_bandwidth: Optional[int] = None
    outgoing_bandwidth: Optional[int] = None


class Settings(BaseModel):
    clients: Optional[List[Dict[str, Any]]] = []
    decryption: Optional[str] = None
    network: Optional[str] = None


class StreamSettings(BaseModel):
    network: Optional[str] = None
    security: Optional[str] = None
    tcpSettings: Optional[Dict[str, Any]] = {}
    wsSettings: Optional[Dict[str, Any]] = {}
    grpcSettings: Optional[Dict[str, Any]] = {}
    tlsSettings: Optional[Dict[str, Any]] = {}
    realitySettings: Optional[Dict[str, Any]] = {}


class Inbound(BaseModel):
    port: Optional[int] = None
    protocol: Optional[str] = None
    settings: Optional[Settings] = Settings()
    streamSettings: Optional[StreamSettings] = StreamSettings()
    sniffing: Optional[Dict[str, Any]] = {}
    tag: Optional[str] = None


class Outbound(BaseModel):
    protocol: Optional[str] = None
    settings: Optional[Dict[str, Any]] = {}
    tag: Optional[str] = None


class RoutingRule(BaseModel):
    type: Optional[str] = None
    ip: Optional[List[str]] = []
    domain: Optional[List[str]] = []
    protocol: Optional[List[str]] = []
    outboundTag: Optional[str] = None


class Routing(BaseModel):
    domainStrategy: Optional[str] = None
    rules: Optional[List[RoutingRule]] = []


class CoreConfig(BaseModel):
    log: Optional[Dict[str, Any]] = {}
    inbounds: Optional[List[Inbound]] = []
    outbounds: Optional[List[Outbound]] = []
    routing: Optional[Routing] = Routing()


# Group
class GroupBase(BaseModel):
    name: str
    inbound_tags: Optional[List[str]] = []
    is_disabled: Optional[bool] = False


class GroupCreate(GroupBase):
    pass


class GroupModify(GroupBase):
    pass


class GroupResponse(GroupBase):
    name: str
    inbound_tags: list
    is_disabled: bool
    id: int
    total_users: Optional[int] = 0


class GroupsResponse(BaseModel):
    groups: List[GroupResponse]
    total: int


class BulkGroup(BaseModel):
    group_ids: List[int]
    has_group_ids: Optional[List[int]] = None
    admins: Optional[List[int]] = None
    users: Optional[List[int]] = None


# Host
class HostBase(BaseModel):
    remark: str
    address: str
    port: Optional[int] = None
    sni: Optional[str] = None
    inbound_tag: Optional[str] = None
    priority: Optional[int] = None


class HostResponse(HostBase):
    id: Optional[int] = None


# Core
class CoreCreate(BaseModel):
    config: Dict[str, Any]
    name: Optional[str] = None
    exclude_inbound_tags: Optional[str] = None
    fallbacks_inbound_tags: Optional[str] = None


class CoreResponse(CoreCreate):
    id: int
    created_at: Optional[str] = None


class CoreResponseList(BaseModel):
    count: int
    cores: List[CoreResponse]


class ModifyUserByTemplate(BaseModel):
    user_template_id: int
    note: Optional[str] = None


class CreateUserFromTemplate(ModifyUserByTemplate):
    username: str


class BulkUser(BaseModel):
    amount: int
    group_ids: Optional[List[int]] = None
    admins: Optional[List[int]] = None
    users: Optional[List[int]] = None
    status: Optional[List[str]] = None


class BulkUsersProxy(BaseModel):
    flow: Optional[str] = None
    method: Optional[str] = None
    group_ids: Optional[List[int]] = None
    admins: Optional[List[int]] = None
    users: Optional[List[int]] = None

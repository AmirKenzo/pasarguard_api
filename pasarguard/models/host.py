from __future__ import annotations

from ._base import (
    Dict,
    ECHQueryStrategy,
    List,
    Optional,
    PasarguardModel,
    ProxyHostALPN,
    ProxyHostFingerprint,
    ProxyHostSecurity,
    RootModel,
    UserStatus,
)
from .proxy import (
    FragmentSettings,
    MuxSettingsInput,
    MuxSettingsOutput,
    NoiseSettings,
    TransportSettingsInput,
    TransportSettingsOutput,
)
from .subscription import SubscriptionTemplates

class BaseHost(PasarguardModel):
    id: Optional[int] = None
    remark: str = ...
    address: Optional[List[str]] = None
    inbound_tag: Optional[str] = None
    port: Optional[int] = None
    sni: Optional[List[str]] = None
    host: Optional[List[str]] = None
    path: Optional[str] = None
    security: Optional[ProxyHostSecurity] = 'inbound_default'
    alpn: Optional[List[ProxyHostALPN]] = None
    fingerprint: Optional[ProxyHostFingerprint] = ''
    allowinsecure: Optional[bool] = None
    is_disabled: Optional[bool] = False
    http_headers: Optional[Dict[str, str]] = None
    transport_settings: Optional[TransportSettingsOutput] = None
    mux_settings: Optional[MuxSettingsOutput] = None
    fragment_settings: Optional[FragmentSettings] = None
    noise_settings: Optional[NoiseSettings] = None
    random_user_agent: Optional[bool] = False
    use_sni_as_host: Optional[bool] = False
    vless_route: Optional[str] = None
    priority: int = ...
    status: Optional[List[UserStatus]] = None
    ech_config_list: Optional[str] = None
    ech_query_strategy: Optional[ECHQueryStrategy] = None
    pinned_peer_cert_sha256: Optional[str] = None
    verify_peer_cert_by_name: Optional[List[str]] = None
    wireguard_overrides: Optional[WireGuardHostOverrides] = None
    subscription_templates: Optional[SubscriptionTemplates] = None

class BulkHostSelection(PasarguardModel):
    ids: Optional[List[int]] = None

class BulkHostsActionResponse(PasarguardModel):
    hosts: List[str] = ...
    count: int = ...

class CreateHost(PasarguardModel):
    id: Optional[int] = None
    remark: str = ...
    address: Optional[List[str]] = None
    inbound_tag: Optional[str] = None
    port: Optional[int] = None
    sni: Optional[List[str]] = None
    host: Optional[List[str]] = None
    path: Optional[str] = None
    security: Optional[ProxyHostSecurity] = 'inbound_default'
    alpn: Optional[List[ProxyHostALPN]] = None
    fingerprint: Optional[ProxyHostFingerprint] = ''
    allowinsecure: Optional[bool] = None
    is_disabled: Optional[bool] = False
    http_headers: Optional[Dict[str, str]] = None
    transport_settings: Optional[TransportSettingsInput] = None
    mux_settings: Optional[MuxSettingsInput] = None
    fragment_settings: Optional[FragmentSettings] = None
    noise_settings: Optional[NoiseSettings] = None
    random_user_agent: Optional[bool] = False
    use_sni_as_host: Optional[bool] = False
    vless_route: Optional[str] = None
    priority: int = ...
    status: Optional[List[UserStatus]] = None
    ech_config_list: Optional[str] = None
    ech_query_strategy: Optional[ECHQueryStrategy] = None
    pinned_peer_cert_sha256: Optional[str] = None
    verify_peer_cert_by_name: Optional[List[str]] = None
    wireguard_overrides: Optional[WireGuardHostOverrides] = None
    subscription_templates: Optional[SubscriptionTemplates] = None

class HostNotificationEnable(PasarguardModel):
    create: Optional[bool] = True
    modify: Optional[bool] = True
    delete: Optional[bool] = True
    modify_hosts: Optional[bool] = True

class RemoveHostsResponse(PasarguardModel):
    hosts: List[str] = ...
    count: int = ...

class WireGuardHostOverrides(PasarguardModel):
    allowed_ips: Optional[List[str]] = None
    mtu: Optional[int] = None
    reserved: Optional[str] = None
    keepalive_seconds: Optional[int] = None
    dns: Optional[List[str]] = None

class HostsModel(RootModel[List[CreateHost]]):
    pass

HostBase = CreateHost
HostResponse = BaseHost

__all__ = (
    'BaseHost',
    'BulkHostSelection',
    'BulkHostsActionResponse',
    'CreateHost',
    'HostNotificationEnable',
    'RemoveHostsResponse',
    'WireGuardHostOverrides',
    'HostsModel',
    'HostBase',
    'HostResponse',
)

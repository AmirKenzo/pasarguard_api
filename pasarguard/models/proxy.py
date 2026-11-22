from __future__ import annotations

from ._base import (
    XUDP,
    Field,
    List,
    MtprotoLinkType,
    MultiplexProtocol,
    Optional,
    PasarguardModel,
    ShadowsocksMethods,
    Union,
    XHttpModes,
)
from .common import HTTPRequest, HTTPResponse


class Brutal(PasarguardModel):
    enable: Optional[bool] = False
    up_mbps: int = ...
    down_mbps: int = ...


class ClashMuxSettings(PasarguardModel):
    enable: Optional[bool] = False
    protocol: Optional[MultiplexProtocol] = "smux"
    max_connections: Optional[int] = None
    max_streams: Optional[int] = None
    min_streams: Optional[int] = None
    padding: Optional[bool] = False
    brutal: Optional[Brutal] = None
    statistic: Optional[bool] = False
    only_tcp: Optional[bool] = False


class ExtraSettings(PasarguardModel):
    method: Optional[ShadowsocksMethods] = "chacha20-ietf-poly1305"


class FragmentSettings(PasarguardModel):
    xray: Optional[XrayFragmentSettings] = None
    sing_box: Optional[SingBoxFragmentSettings] = None


class GRPCSettings(PasarguardModel):
    multi_mode: Optional[bool] = False
    idle_timeout: Optional[int] = None
    health_check_timeout: Optional[int] = None
    permit_without_stream: Optional[bool] = False
    initial_windows_size: Optional[int] = None


class HysteriaSettings(PasarguardModel):
    auth: Optional[str] = None


class KCPSettings(PasarguardModel):
    mtu: Optional[int] = None
    tti: Optional[int] = None
    uplink_capacity: Optional[int] = None
    downlink_capacity: Optional[int] = None
    congestion: Optional[bool] = None
    read_buffer_size: Optional[int] = None
    write_buffer_size: Optional[int] = None


class MasqueHostSettings(PasarguardModel):
    remote_dns: Optional[List[str]] = None
    xmux: Optional[XMuxSettingsOutput] = None


class MasqueSettings(PasarguardModel):
    password: Optional[str] = None


class MtprotoHostSettings(PasarguardModel):
    link_type: Optional[MtprotoLinkType] = MtprotoLinkType.AUTO


class MtprotoSettings(PasarguardModel):
    secret: Optional[str] = None
    user_ad_tag: Optional[str] = ""
    max_tcp_conns: Optional[int] = 0
    max_unique_ips: Optional[int] = 0


class MuxSettingsInput(PasarguardModel):
    sing_box: Optional[SingBoxMuxSettings] = None
    clash: Optional[ClashMuxSettings] = None
    xray: Optional[XrayMuxSettingsInput] = None


class MuxSettingsOutput(PasarguardModel):
    sing_box: Optional[SingBoxMuxSettings] = None
    clash: Optional[ClashMuxSettings] = None
    xray: Optional[XrayMuxSettingsOutput] = None


class NoiseSettings(PasarguardModel):
    xray: Optional[List[XrayNoiseSettings]] = None


class ProxyTable(PasarguardModel):
    vmess: Optional[VMessSettings] = None
    vless: Optional[VlessSettings] = None
    trojan: Optional[TrojanSettings] = None
    shadowsocks: Optional[ShadowsocksSettings] = None
    wireguard: Optional[WireGuardSettings] = None
    hysteria: Optional[HysteriaSettings] = None
    masque: Optional[MasqueSettings] = None
    mtproto: Optional[MtprotoSettings] = None


class ShadowsocksSettings(PasarguardModel):
    password: Optional[str] = None
    method: Optional[ShadowsocksMethods] = "chacha20-ietf-poly1305"


class SingBoxFragmentSettings(PasarguardModel):
    fragment: Optional[bool] = False
    fragment_fallback_delay: Optional[str] = ""
    record_fragment: Optional[bool] = False


class SingBoxMuxSettings(PasarguardModel):
    enable: Optional[bool] = False
    protocol: Optional[MultiplexProtocol] = "smux"
    max_connections: Optional[int] = None
    max_streams: Optional[int] = None
    min_streams: Optional[int] = None
    padding: Optional[bool] = False
    brutal: Optional[Brutal] = None


class TcpSettings(PasarguardModel):
    header: Optional[str] = "none"
    request: Optional[HTTPRequest] = None
    response: Optional[HTTPResponse] = None


class TransportSettingsInput(PasarguardModel):
    xhttp_settings: Optional[XHttpSettingsInput] = None
    grpc_settings: Optional[GRPCSettings] = None
    kcp_settings: Optional[KCPSettings] = None
    tcp_settings: Optional[TcpSettings] = None
    websocket_settings: Optional[WebSocketSettings] = None
    masque_settings: Optional[MasqueHostSettings] = None
    mtproto_settings: Optional[MtprotoHostSettings] = None
    xdrive_settings: Optional[XDriveHostSettings] = None


class TransportSettingsOutput(PasarguardModel):
    xhttp_settings: Optional[XHttpSettingsOutput] = None
    grpc_settings: Optional[GRPCSettings] = None
    kcp_settings: Optional[KCPSettings] = None
    tcp_settings: Optional[TcpSettings] = None
    websocket_settings: Optional[WebSocketSettings] = None
    masque_settings: Optional[MasqueHostSettings] = None
    mtproto_settings: Optional[MtprotoHostSettings] = None
    xdrive_settings: Optional[XDriveHostSettings] = None


class TrojanSettings(PasarguardModel):
    password: Optional[str] = None


class VMessSettings(PasarguardModel):
    id: Optional[str] = None


class VlessSettings(PasarguardModel):
    id: Optional[str] = None


class WebSocketSettings(PasarguardModel):
    heartbeat_period: Optional[int] = Field(None, alias="heartbeatPeriod")


class WireGuardSettings(PasarguardModel):
    private_key: Optional[str] = None
    public_key: Optional[str] = None
    peer_ips: Optional[List[str]] = None


class XDriveHostSettings(PasarguardModel):
    xmux: Optional[XMuxSettingsOutput] = None


class XHttpSettingsInput(PasarguardModel):
    mode: Optional[XHttpModes] = None
    no_grpc_header: Optional[bool] = None
    x_padding_bytes: Optional[Union[str, int]] = None
    x_padding_obfs_mode: Optional[bool] = None
    x_padding_key: Optional[str] = None
    x_padding_header: Optional[str] = None
    x_padding_placement: Optional[str] = None
    x_padding_method: Optional[str] = None
    uplink_http_method: Optional[str] = None
    session_placement: Optional[str] = None
    session_key: Optional[str] = None
    session_id_table: Optional[str] = None
    session_id_length: Optional[Union[str, int]] = None
    seq_placement: Optional[str] = None
    seq_key: Optional[str] = None
    uplink_data_placement: Optional[str] = None
    uplink_data_key: Optional[str] = None
    uplink_chunk_size: Optional[Union[str, int]] = None
    sc_max_each_post_bytes: Optional[Union[str, int]] = None
    sc_min_posts_interval_ms: Optional[Union[str, int]] = None
    xmux: Optional[XMuxSettingsInput] = None
    download_settings: Optional[int] = None


class XHttpSettingsOutput(PasarguardModel):
    mode: Optional[XHttpModes] = None
    no_grpc_header: Optional[bool] = None
    x_padding_bytes: Optional[str] = None
    x_padding_obfs_mode: Optional[bool] = None
    x_padding_key: Optional[str] = None
    x_padding_header: Optional[str] = None
    x_padding_placement: Optional[str] = None
    x_padding_method: Optional[str] = None
    uplink_http_method: Optional[str] = None
    session_placement: Optional[str] = None
    session_key: Optional[str] = None
    session_id_table: Optional[str] = None
    session_id_length: Optional[str] = None
    seq_placement: Optional[str] = None
    seq_key: Optional[str] = None
    uplink_data_placement: Optional[str] = None
    uplink_data_key: Optional[str] = None
    uplink_chunk_size: Optional[str] = None
    sc_max_each_post_bytes: Optional[str] = None
    sc_min_posts_interval_ms: Optional[str] = None
    xmux: Optional[XMuxSettingsOutput] = None
    download_settings: Optional[int] = None


class XMuxSettingsInput(PasarguardModel):
    max_concurrency: Optional[Union[str, int]] = Field(None, alias="maxConcurrency")
    max_connections: Optional[Union[str, int]] = Field(None, alias="maxConnections")
    c_max_reuse_times: Optional[Union[str, int]] = Field(None, alias="cMaxReuseTimes")
    h_max_reusable_secs: Optional[Union[str, int]] = Field(None, alias="hMaxReusableSecs")
    h_max_request_times: Optional[Union[str, int]] = Field(None, alias="hMaxRequestTimes")
    h_keep_alive_period: Optional[int] = Field(None, alias="hKeepAlivePeriod")


class XMuxSettingsOutput(PasarguardModel):
    max_concurrency: Optional[str] = Field(None, alias="maxConcurrency")
    max_connections: Optional[str] = Field(None, alias="maxConnections")
    c_max_reuse_times: Optional[str] = Field(None, alias="cMaxReuseTimes")
    h_max_reusable_secs: Optional[str] = Field(None, alias="hMaxReusableSecs")
    h_max_request_times: Optional[str] = Field(None, alias="hMaxRequestTimes")
    h_keep_alive_period: Optional[int] = Field(None, alias="hKeepAlivePeriod")


class XrayFragmentSettings(PasarguardModel):
    packets: str = ...
    length: str = ...
    interval: str = ...
    max_split: Optional[str] = Field(None, alias="maxSplit")


class XrayMuxSettingsInput(PasarguardModel):
    enabled: Optional[bool] = False
    concurrency: Optional[int] = None
    xudp_concurrency: Optional[int] = None
    xudp_proxy_udp_443: Optional[XUDP] = "reject"


class XrayMuxSettingsOutput(PasarguardModel):
    enabled: Optional[bool] = False
    concurrency: Optional[int] = None
    xudp_concurrency: Optional[int] = Field(None, alias="xudpConcurrency")
    xudp_proxy_u_d_p443: Optional[XUDP] = Field("reject", alias="xudpProxyUDP443")


class XrayNoiseSettings(PasarguardModel):
    type: str = ...
    packet: Optional[Union[str, List[int]]] = None
    delay: Optional[Union[str, int]] = None
    apply_to: Optional[str] = "ip"
    rand: Optional[Union[int, str]] = None
    rand_range: Optional[str] = Field(None, alias="randRange")


VmessSettings = VMessSettings
ProxySettings = ProxyTable

__all__ = (
    "Brutal",
    "ClashMuxSettings",
    "ExtraSettings",
    "FragmentSettings",
    "GRPCSettings",
    "HysteriaSettings",
    "KCPSettings",
    "MasqueHostSettings",
    "MasqueSettings",
    "MtprotoHostSettings",
    "MtprotoSettings",
    "MuxSettingsInput",
    "MuxSettingsOutput",
    "NoiseSettings",
    "ProxySettings",
    "ProxyTable",
    "ShadowsocksSettings",
    "SingBoxFragmentSettings",
    "SingBoxMuxSettings",
    "TcpSettings",
    "TransportSettingsInput",
    "TransportSettingsOutput",
    "TrojanSettings",
    "VMessSettings",
    "VlessSettings",
    "VmessSettings",
    "WebSocketSettings",
    "WireGuardSettings",
    "XDriveHostSettings",
    "XHttpSettingsInput",
    "XHttpSettingsOutput",
    "XMuxSettingsInput",
    "XMuxSettingsOutput",
    "XrayFragmentSettings",
    "XrayMuxSettingsInput",
    "XrayMuxSettingsOutput",
    "XrayNoiseSettings",
)

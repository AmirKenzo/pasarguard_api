from __future__ import annotations

from ._base import (
    DataLimitResetStrategy,
    Dict,
    GeoFilseRegion,
    List,
    NodeConnectionType,
    NodeStatus,
    Optional,
    PasarguardModel,
    Period,
    datetime,
)


class BulkNodeSelection(PasarguardModel):
    ids: Optional[List[int]] = None


class BulkNodesActionResponse(PasarguardModel):
    nodes: List[str] = ...
    count: int = ...


class NodeCoreUpdate(PasarguardModel):
    core_version: Optional[str] = "latest"


class NodeCreate(PasarguardModel):
    name: str = ...
    address: str = ...
    port: Optional[int] = 62050
    api_port: Optional[int] = 62051
    usage_coefficient: Optional[float] = 1.0
    connection_type: NodeConnectionType = ...
    server_ca: str = ...
    keep_alive: int = ...
    core_config_id: int = ...
    api_key: str = ...
    data_limit: Optional[int] = 0
    data_limit_reset_strategy: Optional[DataLimitResetStrategy] = "no_reset"
    reset_time: Optional[int] = -1
    default_timeout: Optional[int] = 10
    internal_timeout: Optional[int] = 15
    proxy_url: Optional[str] = None


class NodeGeoFilesUpdate(PasarguardModel):
    region: Optional[GeoFilseRegion] = "iran"


class NodeModify(PasarguardModel):
    name: Optional[str] = None
    address: Optional[str] = None
    port: Optional[int] = None
    api_port: Optional[int] = 62051
    usage_coefficient: Optional[float] = None
    connection_type: Optional[NodeConnectionType] = None
    server_ca: Optional[str] = None
    keep_alive: Optional[int] = None
    core_config_id: Optional[int] = None
    api_key: Optional[str] = None
    data_limit: Optional[int] = None
    data_limit_reset_strategy: Optional[DataLimitResetStrategy] = None
    reset_time: Optional[int] = None
    default_timeout: Optional[int] = None
    internal_timeout: Optional[int] = None
    proxy_url: Optional[str] = None
    status: Optional[NodeStatus] = None


class NodeNotificationEnable(PasarguardModel):
    create: Optional[bool] = True
    modify: Optional[bool] = True
    delete: Optional[bool] = True
    connect: Optional[bool] = True
    error: Optional[bool] = True
    limited: Optional[bool] = True
    reset_usage: Optional[bool] = True


class NodeOutboundLatency(PasarguardModel):
    name: str = ...
    alive: bool = ...
    delay: int = ...
    link: str = ...
    last_seen_time: int = ...
    last_try_time: int = ...
    source: str = ...


class NodeOutboundsLatencyResponse(PasarguardModel):
    latencies: List[NodeOutboundLatency] = ...


class NodeRealtimeStats(PasarguardModel):
    mem_total: int = ...
    mem_used: int = ...
    cpu_cores: int = ...
    cpu_usage: float = ...
    incoming_bandwidth_speed: int = ...
    outgoing_bandwidth_speed: int = ...
    uptime: int = ...


class NodeResponse(PasarguardModel):
    name: str = ...
    address: str = ...
    port: Optional[int] = 62050
    api_port: Optional[int] = 62051
    usage_coefficient: Optional[float] = 1.0
    connection_type: NodeConnectionType = ...
    server_ca: str = ...
    keep_alive: int = ...
    core_config_id: Optional[int] = ...
    api_key: Optional[str] = ...
    data_limit: Optional[int] = 0
    data_limit_reset_strategy: Optional[DataLimitResetStrategy] = "no_reset"
    reset_time: Optional[int] = -1
    default_timeout: Optional[int] = 10
    internal_timeout: Optional[int] = 15
    proxy_url: Optional[str] = None
    id: int = ...
    xray_version: Optional[str] = ...
    node_version: Optional[str] = ...
    status: NodeStatus = ...
    message: Optional[str] = ...
    uplink: Optional[int] = 0
    downlink: Optional[int] = 0
    lifetime_uplink: Optional[int] = None
    lifetime_downlink: Optional[int] = None
    core_version: Optional[str] = ...


class NodeSettings(PasarguardModel):
    min_node_version: Optional[str] = "v1.0.0"


class NodeSimple(PasarguardModel):
    id: int = ...
    name: str = ...
    status: NodeStatus = ...


class NodeStats(PasarguardModel):
    period_start: datetime = ...
    mem_usage_percentage: float = ...
    cpu_usage_percentage: float = ...
    incoming_bandwidth_speed: float = ...
    outgoing_bandwidth_speed: float = ...


class NodeStatsList(PasarguardModel):
    period: Optional[Period] = None
    start: datetime = ...
    end: datetime = ...
    stats: List[NodeStats] = ...


class NodeUsageStat(PasarguardModel):
    uplink: int = ...
    downlink: int = ...
    period_start: datetime = ...


class NodeUsageStatsList(PasarguardModel):
    period: Optional[Period] = None
    start: datetime = ...
    end: datetime = ...
    stats: Dict[str, List[NodeUsageStat]] = ...


class NodesResponse(PasarguardModel):
    nodes: List[NodeResponse] = ...
    total: int = ...


class NodesSimpleResponse(PasarguardModel):
    nodes: List[NodeSimple] = ...
    total: int = ...


class RemoveNodesResponse(PasarguardModel):
    nodes: List[str] = ...
    count: int = ...


class UserIPList(PasarguardModel):
    ips: Dict[str, int] = ...


class UserIPListAll(PasarguardModel):
    nodes: Dict[str, Optional[UserIPList]] = ...


NodeResponseList = NodesResponse

__all__ = (
    "BulkNodeSelection",
    "BulkNodesActionResponse",
    "NodeCoreUpdate",
    "NodeCreate",
    "NodeGeoFilesUpdate",
    "NodeModify",
    "NodeNotificationEnable",
    "NodeOutboundLatency",
    "NodeOutboundsLatencyResponse",
    "NodeRealtimeStats",
    "NodeResponse",
    "NodeResponseList",
    "NodeSettings",
    "NodeSimple",
    "NodeStats",
    "NodeStatsList",
    "NodeUsageStat",
    "NodeUsageStatsList",
    "NodesResponse",
    "NodesSimpleResponse",
    "RemoveNodesResponse",
    "UserIPList",
    "UserIPListAll",
)

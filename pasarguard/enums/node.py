from __future__ import annotations

from enum import StrEnum


class GeoFilseRegion(StrEnum):
    IRAN = "iran"
    CHINA = "china"
    RUSSIA = "russia"


class NodeConnectionType(StrEnum):
    GRPC = "grpc"
    REST = "rest"


class NodeStatus(StrEnum):
    CONNECTED = "connected"
    CONNECTING = "connecting"
    ERROR = "error"
    DISABLED = "disabled"
    LIMITED = "limited"


class UsageTable(StrEnum):
    NODE_USER_USAGES = "node_user_usages"
    NODE_USAGES = "node_usages"


class UserCountMetric(StrEnum):
    ONLINE = "online"
    EXPIRED = "expired"
    LIMITED = "limited"


__all__ = ("GeoFilseRegion", "NodeConnectionType", "NodeStatus", "UsageTable", "UserCountMetric")

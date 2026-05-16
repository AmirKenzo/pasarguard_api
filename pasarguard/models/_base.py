from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel

from ..enums import (
    ClientTemplateType,
    ConfigFormat,
    CoreType,
    DataLimitResetStrategy,
    ECHQueryStrategy,
    FlowOption,  # noqa: F401 - re-exported for backwards compatibility
    GeoFilseRegion,
    Language,
    MultiplexProtocol,
    NodeConnectionType,
    NodeStatus,
    Period,
    Platform,
    ProxyHostALPN,
    ProxyHostFingerprint,
    ProxyHostSecurity,
    RunMethod,
    ShadowsocksMethod,  # noqa: F401 - re-exported for backwards compatibility
    ShadowsocksMethods,
    UsageTable,  # noqa: F401 - re-exported for API helper annotations
    UserCountMetric,
    UserDataLimitResetStrategy,  # noqa: F401 - re-exported for backwards compatibility
    UserStatus,
    UserStatusCreate,
    UsernameGenerationStrategy,
    XHttpModes,
    XUDP,
)


class PasarguardModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


__all__ = (
    "Any",
    "BaseModel",
    "ConfigDict",
    "Dict",
    "Field",
    "List",
    "Optional",
    "PasarguardModel",
    "RootModel",
    "Union",
    "datetime",
    "ClientTemplateType",
    "ConfigFormat",
    "CoreType",
    "DataLimitResetStrategy",
    "ECHQueryStrategy",
    "FlowOption",
    "GeoFilseRegion",
    "Language",
    "MultiplexProtocol",
    "NodeConnectionType",
    "NodeStatus",
    "Period",
    "Platform",
    "ProxyHostALPN",
    "ProxyHostFingerprint",
    "ProxyHostSecurity",
    "RunMethod",
    "ShadowsocksMethod",
    "ShadowsocksMethods",
    "UsageTable",
    "UserCountMetric",
    "UserDataLimitResetStrategy",
    "UserStatus",
    "UserStatusCreate",
    "UsernameGenerationStrategy",
    "XHttpModes",
    "XUDP",
)
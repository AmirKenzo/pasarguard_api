from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel

from ..enums import (
    XUDP,
    ClientTemplateType,
    ConfigFormat,
    CoreType,
    DataLimitResetStrategy,
    ECHQueryStrategy,
    FlowOption,
    GeoFilseRegion,
    HeaderPlacement,
    HWIDMode,
    Language,
    MtprotoLinkType,
    MultiplexProtocol,
    NodeConnectionType,
    NodeStatus,
    OnHoldTimeoutAction,
    Period,
    Platform,
    ProxyHostALPN,
    ProxyHostFingerprint,
    ProxyHostSecurity,
    RunMethod,
    ShadowsocksMethod,
    ShadowsocksMethods,
    UsageTable,
    UserCountMetric,
    UserDataLimitResetStrategy,
    UsernameGenerationStrategy,
    UserStatus,
    UserStatusCreate,
    XHttpModes,
)

Dict = dict
List = list


class PasarguardModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


__all__ = (
    "XUDP",
    "Any",
    "BaseModel",
    "ClientTemplateType",
    "ConfigDict",
    "ConfigFormat",
    "CoreType",
    "DataLimitResetStrategy",
    "Dict",
    "ECHQueryStrategy",
    "Field",
    "FlowOption",
    "GeoFilseRegion",
    "HWIDMode",
    "HeaderPlacement",
    "Language",
    "List",
    "MtprotoLinkType",
    "MultiplexProtocol",
    "NodeConnectionType",
    "NodeStatus",
    "OnHoldTimeoutAction",
    "Optional",
    "PasarguardModel",
    "Period",
    "Platform",
    "ProxyHostALPN",
    "ProxyHostFingerprint",
    "ProxyHostSecurity",
    "RootModel",
    "RunMethod",
    "ShadowsocksMethod",
    "ShadowsocksMethods",
    "Union",
    "UsageTable",
    "UserCountMetric",
    "UserDataLimitResetStrategy",
    "UserStatus",
    "UserStatusCreate",
    "UsernameGenerationStrategy",
    "XHttpModes",
    "datetime",
)

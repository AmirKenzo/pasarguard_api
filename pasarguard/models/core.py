from __future__ import annotations

from ._base import Any, CoreType, Dict, Field, List, Optional, PasarguardModel, datetime


class BulkCoreSelection(PasarguardModel):
    ids: Optional[List[int]] = None


class CoreCreate(PasarguardModel):
    name: Optional[str] = None
    config: Dict[str, Any] = ...
    type: Optional[CoreType] = None
    exclude_inbound_tags: Optional[List[Any]] = None
    fallbacks_inbound_tags: Optional[List[Any]] = None


class CoreResponse(PasarguardModel):
    name: str = ...
    config: Dict[str, Any] = ...
    type: Optional[CoreType] = None
    exclude_inbound_tags: List[str] = ...
    fallbacks_inbound_tags: List[str] = ...
    id: int = ...
    created_at: datetime = ...


class CoreResponseList(PasarguardModel):
    count: int = ...
    cores: Optional[List[CoreResponse]] = Field(default_factory=list)


class CoreSimple(PasarguardModel):
    id: int = ...
    name: str = ...
    type: Optional[CoreType] = None


class CoresSimpleResponse(PasarguardModel):
    cores: List[CoreSimple] = ...
    total: int = ...


class RealityScanRequest(PasarguardModel):
    target: str = ...
    timeout: Optional[float] = None


class RealityScanResult(PasarguardModel):
    target: str = ...
    host: str = ...
    ip: Optional[str] = None
    port: int = ...
    sni: Optional[str] = None
    sni_discovered: Optional[bool] = False
    feasible: bool = ...
    tls13: bool = ...
    tls_version: Optional[str] = None
    h2: bool = ...
    alpn: Optional[str] = None
    x25519: Optional[bool] = None
    post_quantum: Optional[bool] = None
    curve: Optional[str] = None
    h3: Optional[bool] = False
    cert_valid: bool = ...
    cert_subject: Optional[str] = None
    cert_issuer: Optional[str] = None
    not_after: Optional[str] = None
    server_names: Optional[List[str]] = Field(default_factory=list)
    latency_ms: Optional[int] = None
    reason: Optional[str] = None


class RemoveCoresResponse(PasarguardModel):
    cores: List[str] = ...
    count: int = ...


__all__ = (
    "BulkCoreSelection",
    "CoreCreate",
    "CoreResponse",
    "CoreResponseList",
    "CoreSimple",
    "CoresSimpleResponse",
    "RealityScanRequest",
    "RealityScanResult",
    "RemoveCoresResponse",
)

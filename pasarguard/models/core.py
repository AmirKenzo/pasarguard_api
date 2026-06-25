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
    "RemoveCoresResponse",
)

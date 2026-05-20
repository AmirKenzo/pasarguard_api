from __future__ import annotations

from ._base import List, Optional, PasarguardModel, datetime

class UserHWIDListResponse(PasarguardModel):
    hwids: List[UserHWIDResponse] = ...
    count: int = ...

class UserHWIDResponse(PasarguardModel):
    id: int = ...
    hwid: str = ...
    device_os: Optional[str] = None
    os_version: Optional[str] = None
    device_model: Optional[str] = None
    created_at: datetime = ...
    last_used_at: datetime = ...

__all__ = (
    'UserHWIDListResponse',
    'UserHWIDResponse',
)

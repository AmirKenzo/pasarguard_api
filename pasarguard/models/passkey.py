from __future__ import annotations

from ._base import Any, Dict, Optional, PasarguardModel


class PasskeyInfo(PasarguardModel):
    id: int = ...
    name: str = ...


class PasskeyOptionsRequest(PasarguardModel):
    username: Optional[str] = None


class PasskeyRegistrationRequest(PasarguardModel):
    credential: Dict[str, Any] = ...
    name: Optional[str] = "This device"


class PasskeyAuthenticationRequest(PasarguardModel):
    username: Optional[str] = None
    credential: Dict[str, Any] = ...


__all__ = (
    "PasskeyAuthenticationRequest",
    "PasskeyInfo",
    "PasskeyOptionsRequest",
    "PasskeyRegistrationRequest",
)

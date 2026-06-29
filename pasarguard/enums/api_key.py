from __future__ import annotations

from enum import StrEnum


class APIKeyStatus(StrEnum):
    ACTIVE = "active"
    DISABLED = "disabled"


__all__ = ("APIKeyStatus",)

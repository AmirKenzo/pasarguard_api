from __future__ import annotations

from enum import StrEnum


class CoreType(StrEnum):
    XRAY = 'xray'
    WG = 'wg'
    MTPROTO = 'mtproto'
    SINGBOX = 'singbox'


__all__ = ("CoreType",)
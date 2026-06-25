from __future__ import annotations

from enum import StrEnum


class ConfigFormat(StrEnum):
    LINKS = "links"
    LINKS_BASE64 = "links_base64"
    XRAY = "xray"
    WIREGUARD = "wireguard"
    SING_BOX = "sing_box"
    CLASH = "clash"
    CLASH_META = "clash_meta"
    OUTLINE = "outline"
    BLOCK = "block"


class Language(StrEnum):
    FA = "fa"
    EN = "en"
    RU = "ru"
    ZH = "zh"


class Period(StrEnum):
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"
    MONTH = "month"


class Platform(StrEnum):
    ANDROID = "android"
    IOS = "ios"
    WINDOWS = "windows"
    MACOS = "macos"
    LINUX = "linux"
    APPLETV = "appletv"
    ANDROIDTV = "androidtv"


class RunMethod(StrEnum):
    WEBHOOK = "webhook"
    LONG_POLLING = "long-polling"


class HWIDMode(StrEnum):
    DISABLED = "disabled"
    USE_GLOBAL = "use_global"
    OVERRIDE = "override"


__all__ = ("ConfigFormat", "HWIDMode", "Language", "Period", "Platform", "RunMethod")

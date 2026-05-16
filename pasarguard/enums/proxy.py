from __future__ import annotations

from enum import StrEnum


class ECHQueryStrategy(StrEnum):
    NONE = 'none'
    HALF = 'half'
    FULL = 'full'


class MultiplexProtocol(StrEnum):
    SMUX = 'smux'
    YAMUX = 'yamux'
    H2MUX = 'h2mux'


class ProxyHostALPN(StrEnum):
    HTTP_1_1 = 'http/1.1'
    H2 = 'h2'
    H3 = 'h3'


class ProxyHostFingerprint(StrEnum):
    EMPTY = ''
    CHROME = 'chrome'
    FIREFOX = 'firefox'
    SAFARI = 'safari'
    IOS = 'ios'
    ANDROID = 'android'
    EDGE = 'edge'
    _360 = '360'
    QQ = 'qq'
    RANDOM = 'random'
    RANDOMIZED = 'randomized'
    RANDOMIZEDNOALPN = 'randomizednoalpn'
    UNSAFE = 'unsafe'


class ProxyHostSecurity(StrEnum):
    INBOUND_DEFAULT = 'inbound_default'
    NONE = 'none'
    TLS = 'tls'


class ShadowsocksMethods(StrEnum):
    AES_128_GCM = 'aes-128-gcm'
    AES_256_GCM = 'aes-256-gcm'
    CHACHA20_IETF_POLY1305 = 'chacha20-ietf-poly1305'
    XCHACHA20_POLY1305 = 'xchacha20-poly1305'


class XHttpModes(StrEnum):
    AUTO = 'auto'
    PACKET_UP = 'packet-up'
    STREAM_UP = 'stream-up'
    STREAM_ONE = 'stream-one'


class XUDP(StrEnum):
    REJECT = 'reject'
    ALLOW = 'allow'
    SKIP = 'skip'


class FlowOption(StrEnum):
    NONE = ""
    XTLS_RPRX_VISION = "xtls-rprx-vision"


ShadowsocksMethod = ShadowsocksMethods


__all__ = (
    "ECHQueryStrategy",
    "FlowOption",
    "MultiplexProtocol",
    "ProxyHostALPN",
    "ProxyHostFingerprint",
    "ProxyHostSecurity",
    "ShadowsocksMethod",
    "ShadowsocksMethods",
    "XHttpModes",
    "XUDP",
)
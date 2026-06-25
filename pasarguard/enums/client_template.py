from __future__ import annotations

from enum import StrEnum


class ClientTemplateType(StrEnum):
    CLASH_SUBSCRIPTION = "clash_subscription"
    XRAY_SUBSCRIPTION = "xray_subscription"
    SINGBOX_SUBSCRIPTION = "singbox_subscription"
    USER_AGENT = "user_agent"
    GRPC_USER_AGENT = "grpc_user_agent"


__all__ = ("ClientTemplateType",)

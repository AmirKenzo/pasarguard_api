from __future__ import annotations

from .admin import AdminMixin
from .admin_role import AdminRoleMixin
from .base import BaseAPIClient
from .client_template import ClientTemplateMixin
from .compat import CompatibilityMixin
from .core import CoreMixin
from .default import DefaultMixin
from .groups import GroupsMixin
from .host import HostMixin
from .node import NodeMixin
from .settings import SettingsMixin
from .setup import SetupMixin
from .subscription import SubscriptionMixin
from .system import SystemMixin
from .user import UserMixin
from .user_hwid import UserHWIDMixin
from .user_template import UserTemplateMixin


class PasarguardAPI(
    CompatibilityMixin,
    SetupMixin,
    AdminRoleMixin,
    UserHWIDMixin,
    UserTemplateMixin,
    SubscriptionMixin,
    UserMixin,
    NodeMixin,
    HostMixin,
    ClientTemplateMixin,
    CoreMixin,
    GroupsMixin,
    SettingsMixin,
    SystemMixin,
    AdminMixin,
    DefaultMixin,
    BaseAPIClient,
):
    pass


__all__ = ("PasarguardAPI",)

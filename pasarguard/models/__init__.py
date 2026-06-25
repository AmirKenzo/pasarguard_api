from __future__ import annotations

# Public model facade. Definitions live in section modules; this keeps old imports stable.
# ruff: noqa: F401, F403
from pydantic import BaseModel

from ._base import PasarguardModel
from .admin import *
from .admin_role import *
from .client_template import *
from .common import *
from .core import *
from .groups import *
from .host import *
from .node import *
from .proxy import *
from .settings import *
from .subscription import *
from .system import *
from .user import *
from .user_hwid import *
from .user_template import *


def _rebuild_models() -> None:
    namespace = globals()
    for name, value in tuple(namespace.items()):
        if name == "BaseModel":
            continue
        if isinstance(value, type) and issubclass(value, BaseModel):
            value.model_rebuild(force=True, _types_namespace=namespace)


_rebuild_models()

__all__ = tuple(
    name for name, value in globals().items() if not name.startswith("_") and name not in {"BaseModel", "annotations"}
)

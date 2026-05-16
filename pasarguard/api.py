from __future__ import annotations

# Compatibility module: public users can still import PasarguardAPI and generated models/enums here.
# ruff: noqa: F401, F403

from .client import PasarguardAPI
from .enums import *
from .models import *

__all__ = tuple(name for name in globals() if not name.startswith("_") and name != "annotations")
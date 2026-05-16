from __future__ import annotations

# ruff: noqa: F401, F403
from ._base import *

class BulkGroup(PasarguardModel):
    group_ids: List[int] = ...
    has_group_ids: Optional[List[int]] = None
    admins: Optional[List[int]] = None
    users: Optional[List[int]] = None
    dry_run: Optional[bool] = False

class BulkGroupSelection(PasarguardModel):
    ids: Optional[List[int]] = None

class BulkGroupsActionResponse(PasarguardModel):
    groups: List[str] = ...
    count: int = ...

class GroupCreate(PasarguardModel):
    name: str = ...
    inbound_tags: List[str] = ...
    is_disabled: Optional[bool] = False

class GroupModify(PasarguardModel):
    name: str = ...
    inbound_tags: Optional[List[str]] = []
    is_disabled: Optional[bool] = False

class GroupResponse(PasarguardModel):
    name: str = ...
    inbound_tags: Optional[List[str]] = []
    is_disabled: Optional[bool] = False
    id: int = ...
    total_users: Optional[int] = 0

class GroupSimple(PasarguardModel):
    id: int = ...
    name: str = ...

class GroupsResponse(PasarguardModel):
    groups: List[GroupResponse] = ...
    total: int = ...

class GroupsSimpleResponse(PasarguardModel):
    groups: List[GroupSimple] = ...
    total: int = ...

class RemoveGroupsResponse(PasarguardModel):
    groups: List[str] = ...
    count: int = ...

__all__ = (
    'BulkGroup',
    'BulkGroupSelection',
    'BulkGroupsActionResponse',
    'GroupCreate',
    'GroupModify',
    'GroupResponse',
    'GroupSimple',
    'GroupsResponse',
    'GroupsSimpleResponse',
    'RemoveGroupsResponse',
)

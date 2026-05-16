from __future__ import annotations

from enum import StrEnum


class DataLimitResetStrategy(StrEnum):
    NO_RESET = 'no_reset'
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    YEAR = 'year'


class UserStatus(StrEnum):
    ACTIVE = 'active'
    DISABLED = 'disabled'
    LIMITED = 'limited'
    EXPIRED = 'expired'
    ON_HOLD = 'on_hold'


class UserStatusCreate(StrEnum):
    ACTIVE = 'active'
    ON_HOLD = 'on_hold'


class UsernameGenerationStrategy(StrEnum):
    RANDOM = 'random'
    SEQUENCE = 'sequence'


UserDataLimitResetStrategy = DataLimitResetStrategy


__all__ = (
    "DataLimitResetStrategy",
    "UserDataLimitResetStrategy",
    "UserStatus",
    "UserStatusCreate",
    "UsernameGenerationStrategy",
)
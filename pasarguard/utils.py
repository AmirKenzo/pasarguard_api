import logging
import re
import secrets
import string
import time
from datetime import datetime, timedelta
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pasarguard import PasarguardAPI


Number = int | float

_SIZE_UNITS = {
    "mb": 1024**2,
    "mib": 1024**2,
    "gb": 1024**3,
    "gib": 1024**3,
    "tb": 1024**4,
    "tib": 1024**4,
}

_TIME_UNITS = {
    "m": 60,
    "min": 60,
    "minute": 60,
    "minutes": 60,
    "h": 60 * 60,
    "hour": 60 * 60,
    "hours": 60 * 60,
    "d": 24 * 60 * 60,
    "day": 24 * 60 * 60,
    "days": 24 * 60 * 60,
}


def _parse_amount_unit(value: str) -> tuple[float, str]:
    match = re.fullmatch(r"\s*([0-9]+(?:\.[0-9]+)?)\s*([A-Za-z]+)\s*", value)
    if not match:
        raise ValueError(f"invalid value with unit: {value!r}")
    return float(match.group(1)), match.group(2).lower()


def to_bytes(value: str | Number, unit: str | None = None) -> int:
    if isinstance(value, str):
        amount, parsed_unit = _parse_amount_unit(value)
        unit_key = parsed_unit
    else:
        amount = float(value)
        unit_key = (unit or "gb").lower()
    if amount < 0:
        raise ValueError("size cannot be negative")
    try:
        multiplier = _SIZE_UNITS[unit_key]
    except KeyError as exc:
        raise ValueError(f"unsupported size unit: {unit_key!r}") from exc
    return int(amount * multiplier)


def mb(value: Number) -> int:
    return to_bytes(value, "mb")


def gb(value: Number) -> int:
    return to_bytes(value, "gb")


def tb(value: Number) -> int:
    return to_bytes(value, "tb")


def _duration_seconds(value: str | Number, unit: str | None = None) -> int:
    if isinstance(value, str):
        amount, parsed_unit = _parse_amount_unit(value)
        unit_key = parsed_unit
    else:
        amount = float(value)
        unit_key = (unit or "d").lower()
    if amount < 0:
        raise ValueError("duration cannot be negative")
    try:
        multiplier = _TIME_UNITS[unit_key]
    except KeyError as exc:
        raise ValueError(f"unsupported time unit: {unit_key!r}") from exc
    return int(amount * multiplier)


def to_timestamp(value: str | Number, unit: str | None = None, *, now: Number | None = None) -> int:
    current = int(time.time() if now is None else now)
    return current + _duration_seconds(value, unit)


def minutes(value: Number) -> int:
    return to_timestamp(value, "m")


def hours(value: Number) -> int:
    return to_timestamp(value, "h")


def days(value: Number) -> int:
    return to_timestamp(value, "d")


def random_username(
    prefix: str = "user",
    *,
    length: int = 8,
    separator: str = "_",
    alphabet: str = string.ascii_lowercase + string.digits,
) -> str:
    if length <= 0:
        raise ValueError("length must be greater than zero")
    if not alphabet:
        raise ValueError("alphabet cannot be empty")

    suffix = "".join(secrets.choice(alphabet) for _ in range(length))
    if not prefix:
        return suffix
    return f"{prefix}{separator}{suffix}"


class PasarguardTokenCache:
    def __init__(
        self,
        client: "PasarguardAPI",
        username: str | None = None,
        password: str | None = None,
        api_key: str | None = None,
        token_expire_minutes: int = 1440,
    ):
        if api_key and (username or password):
            raise ValueError("Provide either api_key or username/password for PasarguardTokenCache")
        if not api_key and not (username and password):
            raise ValueError("PasarguardTokenCache requires api_key or username and password")
        self._client = client
        self._username = username
        self._password = password
        self._api_key = api_key
        self._token_expire_minutes = token_expire_minutes
        self._token: str | None = None
        self._exp_at: datetime | None = None

    async def get_token(self):
        if self._api_key:
            return self._api_key
        if not self._exp_at or self._exp_at < datetime.now():
            logging.info("Get new token")
            self._token = await self.get_new_token()
            self._exp_at = datetime.now() + timedelta(minutes=self._token_expire_minutes - 1)
        return self._token

    async def get_new_token(self):
        if self._api_key:
            return self._api_key
        try:
            token = await self._client.get_token(username=self._username, password=self._password)
            return token.access_token
        except Exception as e:
            logging.error(f"{e}", exc_info=True)
            raise


class Tools:
    to_bytes = staticmethod(to_bytes)
    mb = staticmethod(mb)
    gb = staticmethod(gb)
    tb = staticmethod(tb)
    to_timestamp = staticmethod(to_timestamp)
    minutes = staticmethod(minutes)
    hours = staticmethod(hours)
    days = staticmethod(days)
    random_username = staticmethod(random_username)


__all__ = (
    "PasarguardTokenCache",
    "Tools",
)

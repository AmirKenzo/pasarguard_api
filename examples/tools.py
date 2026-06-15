"""Convenience helpers for traffic, expiration timestamps, usernames, and group assignment.

Run:
  uv run python examples/tools.py
"""

from __future__ import annotations

import asyncio
import os

from pasarguard import PasarguardAPI, Tools, UserCreate, UserStatus


def preview_user_payload() -> None:
    user = UserCreate(
        username=Tools.random_username(prefix="trial"),
        data_limit=Tools.gb(20),
        expire=Tools.days(30),
        status=UserStatus.ACTIVE,
        note="Created with SDK tools",
    )

    print("20 MB:", Tools.mb(20))
    print("20 GB:", Tools.gb(20))
    print("1 TB:", Tools.tb(1))
    print("expires in 30 minutes:", Tools.minutes(30))
    print("expires in 12 hours:", Tools.hours(12))
    print("expires in 30 days:", Tools.days(30))
    print("from string:", Tools.to_bytes("500MB"), Tools.to_timestamp("12h"))
    print("user payload:", user.model_dump(mode="json", exclude_none=True))


async def create_user_in_all_groups() -> None:
    base_url = os.environ["PASARGUARD_BASE_URL"]
    admin_username = os.environ["PASARGUARD_ADMIN_USERNAME"]
    admin_password = os.environ["PASARGUARD_ADMIN_PASSWORD"]

    async with PasarguardAPI(base_url=base_url) as api:
        token = (await api.get_token(admin_username, admin_password)).access_token
        user = await api.create_user_in_all_groups(
            UserCreate(
                username=Tools.random_username(prefix="customer"),
                data_limit=Tools.gb(20),
                expire=Tools.days(30),
                status=UserStatus.ACTIVE,
                note="Created in all groups",
            ),
            token=token,
        )
        print("created:", user.id, user.username)


async def main() -> None:
    preview_user_payload()

    required_env = {
        "PASARGUARD_BASE_URL",
        "PASARGUARD_ADMIN_USERNAME",
        "PASARGUARD_ADMIN_PASSWORD",
    }
    if required_env <= set(os.environ):
        await create_user_in_all_groups()
    else:
        print("Set PASARGUARD_* env vars to create a real user in all groups.")


if __name__ == "__main__":
    asyncio.run(main())

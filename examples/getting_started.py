"""
Getting started with the Pasarguard SDK.

Shows how to create a client, obtain a token, and create a user.

Run: python getting_started.py
"""

from __future__ import annotations

import asyncio
import os
from uuid import uuid4

from pasarguard import PasarguardAPI, UserCreate, UserStatus

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")
ADMIN_USERNAME = os.environ.get("PASARGUARD_ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("PASARGUARD_ADMIN_PASSWORD", "password")


async def main() -> None:
    # Recommended: use async with so the client closes automatically.
    async with PasarguardAPI(
        base_url=BASE_URL,
        verify=True,
        timeout=30.0,
    ) as api:
        # get_token: obtain a Bearer token for admin API calls
        token = (await api.get_token(ADMIN_USERNAME, ADMIN_PASSWORD)).access_token

        # admin_token is an alias for get_token
        await api.admin_token(ADMIN_USERNAME, ADMIN_PASSWORD)

        # Fetch groups so the new user can be assigned to at least one group
        groups = await api.get_groups_simple(token=token)
        group_ids = [g.id for g in groups.groups] if groups.groups else []

        username = f"example_{uuid4().hex[:8]}"
        user = await api.create_user(
            UserCreate(
                username=username,
                group_ids=group_ids,
                status=UserStatus.ACTIVE,
                note="Created from examples/getting_started.py",
            ),
            token=token,
        )
        print(f"Created user: {user.username}")
        print(f"Subscription URL: {user.subscription_url}")

        admin = await api.get_current_admin(token=token)
        print(f"Logged in as: {admin.username}")


if __name__ == "__main__":
    asyncio.run(main())

"""
API keys — authenticate without admin login.

Pass api_key when creating the client; all admin methods use it automatically
(no need to call get_token or pass token= on every call).

Run: python api_keys.py
"""

from __future__ import annotations

import asyncio
import os
from uuid import uuid4

from pasarguard import PasarguardAPI, UserCreate, UserStatus

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")
API_KEY = os.environ.get("PASARGUARD_API_KEY", "pg_key_your_key_here")


async def main() -> None:
    async with PasarguardAPI(
        base_url=BASE_URL,
        api_key=API_KEY,
        verify=True,
        timeout=30.0,
    ) as api:
        # No login — api_key is sent as Bearer on every admin request
        admin = await api.get_current_admin()
        print(f"OK get_current_admin -> {admin.username}")

        groups = await api.get_groups_simple()
        group_ids = [g.id for g in groups.groups] if groups.groups else []

        user = await api.create_user(
            UserCreate(
                username=f"apikey_demo_{uuid4().hex[:8]}",
                group_ids=group_ids,
                status=UserStatus.ACTIVE,
                note="Created via API key (no JWT login)",
            ),
        )
        print(f"OK create_user -> {user.username}")

        keys = await api.list_api_keys()
        print(f"OK list_api_keys -> {keys.total} key(s)")

        # Optional: override per call with a different token
        # other = await api.get_current_admin(token="another-jwt-or-api-key")

        print("\nDone — API key auth works without get_token()")


if __name__ == "__main__":
    asyncio.run(main())

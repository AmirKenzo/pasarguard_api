"""
User HWID (device) management.

Methods covered:
- get_user_hwids
- delete_user_hwid
- reset_user_hwids

Run: python user_hwid.py
"""

from __future__ import annotations

import asyncio
import os

from pasarguard import PasarguardAPI

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")
ADMIN_USERNAME = os.environ.get("PASARGUARD_ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("PASARGUARD_ADMIN_PASSWORD", "password")


async def main() -> None:
    async with PasarguardAPI(base_url=BASE_URL, verify=True, timeout=30.0) as api:
        token = (await api.get_token(ADMIN_USERNAME, ADMIN_PASSWORD)).access_token

        users = await api.get_users_simple(token=token, limit=1)
        if not users.users:
            print("No users found")
            return

        user_id = users.users[0].id
        print(f"User id={user_id}\n")

        hwids = await api.get_user_hwids(user_id=user_id, token=token)
        print(f"OK get_user_hwids -> {len(hwids.hwids)} devices")

        if hwids.hwids:
            first_hwid = hwids.hwids[0].hwid
            # await api.delete_user_hwid(user_id=user_id, hwid=first_hwid, token=token)
            print(f"INFO delete_user_hwid — hwid={first_hwid[:16]}... (commented out)")

        # await api.reset_user_hwids(user_id=user_id, token=token)
        print("INFO reset_user_hwids — commented out")

        print("\nDone — user HWID reviewed")


if __name__ == "__main__":
    asyncio.run(main())

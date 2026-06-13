"""
Initial panel setup (owner management).

These endpoints are only used during first-time setup and require a setup key.

Methods covered:
- create_owner
- delete_owner
- upgrade_owner
- reset_owner_password

Run: python setup.py
"""

from __future__ import annotations

import asyncio
import os

from pasarguard import PasarguardAPI

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")
SETUP_KEY = os.environ.get("PASARGUARD_SETUP_KEY", "")


async def main() -> None:
    if not SETUP_KEY:
        print("PASARGUARD_SETUP_KEY is not set — showing method signatures only\n")

    async with PasarguardAPI(base_url=BASE_URL, verify=True, timeout=30.0) as api:
        # owner = await api.create_owner(
        #     OwnerCreateRequest(key=SETUP_KEY, username="admin", password="SecurePassword123!")
        # )
        print("INFO create_owner(OwnerCreateRequest(key, username, password))")

        # owner = await api.upgrade_owner(OwnerUpgradeRequest(key=SETUP_KEY, username="admin"))
        print("INFO upgrade_owner(OwnerUpgradeRequest(key, username))")

        # owner = await api.reset_owner_password(OwnerResetRequest(key=SETUP_KEY, password="NewPassword123!"))
        print("INFO reset_owner_password(OwnerResetRequest(key, password))")

        # await api.delete_owner(key=SETUP_KEY)
        print("INFO delete_owner(key)")

        print("\nDone — setup methods documented (not executed)")


if __name__ == "__main__":
    asyncio.run(main())

"""
Panel settings.

Methods covered:
- get_settings, modify_settings, get_general_settings

Run: python settings.py
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

        settings = await api.get_settings(token=token)
        print(f"OK get_settings -> {type(settings).__name__}")

        await api.get_general_settings(token=token)
        print("OK get_general_settings")

        # Warning: modifies global panel settings
        # await api.modify_settings(settings=settings, token=token)

        print("INFO modify_settings — commented out (destructive)")
        print("\nDone — settings reviewed")


if __name__ == "__main__":
    asyncio.run(main())

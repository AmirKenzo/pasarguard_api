"""
System statistics and inbounds.

Methods covered:
- get_system_stats, get_inbounds, get_inbound_details, get_workers_health

Run: python system.py
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

        stats = await api.get_system_stats(token=token)
        print(f"OK get_system_stats -> total_user={stats.total_user}")

        inbounds = await api.get_inbounds(token=token)
        print(f"OK get_inbounds -> {len(inbounds)} inbounds")

        details = await api.get_inbound_details(token=token)
        print(f"OK get_inbound_details -> {len(details)} inbounds")

        await api.get_workers_health(token=token)
        print("OK get_workers_health")

        print("\nDone — system reviewed")


if __name__ == "__main__":
    asyncio.run(main())

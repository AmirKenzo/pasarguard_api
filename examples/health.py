"""
API health checks (no admin token required).

Methods covered:
- base
- health

Run: python health.py
"""

from __future__ import annotations

import asyncio
import os

from pasarguard import PasarguardAPI

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")


async def main() -> None:
    async with PasarguardAPI(base_url=BASE_URL, verify=True, timeout=30.0) as api:
        base_info = await api.base()
        print("base:", base_info)

        health = await api.health()
        print("health:", health)


if __name__ == "__main__":
    asyncio.run(main())

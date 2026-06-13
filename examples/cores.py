"""
Core configuration management.

Methods covered:
- create_core_config, get_core_config, modify_core_config, delete_core_config
- get_all_cores, get_cores_simple
- restart_core, bulk_delete_cores

Run: python cores.py
"""

from __future__ import annotations

import asyncio
import os

from pasarguard import BulkCoreSelection, PasarguardAPI

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")
ADMIN_USERNAME = os.environ.get("PASARGUARD_ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("PASARGUARD_ADMIN_PASSWORD", "password")


async def main() -> None:
    async with PasarguardAPI(base_url=BASE_URL, verify=True, timeout=30.0) as api:
        token = (await api.get_token(ADMIN_USERNAME, ADMIN_PASSWORD)).access_token

        cores = await api.get_all_cores(token=token, limit=10)
        print(f"OK get_all_cores -> {len(cores.cores)} cores")

        simple = await api.get_cores_simple(token=token, limit=10)
        print(f"OK get_cores_simple -> {len(simple.cores)} cores")

        if not simple.cores:
            return

        core_id = simple.cores[0].id
        core = await api.get_core_config(core_id=core_id, token=token)
        print(f"OK get_core_config -> {core.name}")

        bulk = BulkCoreSelection(ids=[core_id])
        # await api.create_core_config(CoreCreate(...), token=token)
        # await api.modify_core_config(core_id, CoreCreate(...), restart_nodes=False, token=token)
        # await api.restart_core(core_id=core_id, token=token)
        # await api.delete_core_config(core_id=core_id, token=token, restart_nodes=False)
        # await api.bulk_delete_cores(bulk, token=token)

        print("INFO create/modify/delete/restart — commented out")
        print("\nDone — cores reviewed")


if __name__ == "__main__":
    asyncio.run(main())

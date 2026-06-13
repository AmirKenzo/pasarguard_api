"""
Host management.

Methods covered:
- get_host, get_hosts, create_host, modify_host, modify_hosts, remove_host
- bulk_delete_hosts, bulk_disable_hosts, bulk_enable_hosts

Run: python hosts.py
"""

from __future__ import annotations

import asyncio
import os

from pasarguard import BulkHostSelection, PasarguardAPI

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")
ADMIN_USERNAME = os.environ.get("PASARGUARD_ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("PASARGUARD_ADMIN_PASSWORD", "password")


async def main() -> None:
    async with PasarguardAPI(base_url=BASE_URL, verify=True, timeout=30.0) as api:
        token = (await api.get_token(ADMIN_USERNAME, ADMIN_PASSWORD)).access_token

        hosts = await api.get_hosts(token=token, limit=10)
        print(f"OK get_hosts -> {len(hosts)} hosts")

        if hosts:
            host_id = hosts[0].id
            host = await api.get_host(host_id=host_id, token=token)
            print(f"OK get_host -> id={host.id}")

            bulk = BulkHostSelection(ids=[host_id])
            # await api.bulk_disable_hosts(bulk, token=token)
            # await api.bulk_enable_hosts(bulk, token=token)
            # await api.bulk_delete_hosts(bulk, token=token)

        # await api.create_host(CreateHost(...), token=token)
        # await api.modify_host(host_id=host_id, host=CreateHost(...), token=token)
        # await api.modify_hosts(hosts=[CreateHost(...)], token=token)
        # await api.remove_host(host_id=host_id, token=token)

        print("INFO create/modify/remove/bulk — commented out")
        print("\nDone — hosts reviewed")


if __name__ == "__main__":
    asyncio.run(main())

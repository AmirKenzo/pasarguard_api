"""
Backward-compatible method aliases.

Legacy names that delegate to the current API:

- add_user -> create_user
- activate_next_plan -> active_next_plan
- get_user_data_usage -> get_user_usage
- update_node_core -> update_core
- update_node_geofiles -> update_geofiles
- get_user_subscription_info -> user_subscription_info
- get_sub_user_usage_by_url -> get_sub_user_usage
- get_user_subscription_with_client_type -> user_subscription_with_client_type

Run: python legacy_aliases.py
"""

from __future__ import annotations

import asyncio
import os
from uuid import uuid4

from pasarguard import ConfigFormat, PasarguardAPI, Period, UserCreate

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")
ADMIN_USERNAME = os.environ.get("PASARGUARD_ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("PASARGUARD_ADMIN_PASSWORD", "password")


def extract_sub_token(subscription_url: str | None) -> str | None:
    if not subscription_url:
        return None
    parts = subscription_url.rstrip("/").split("/")
    if len(parts) >= 2 and parts[-2] == "sub":
        return parts[-1]
    return parts[-1] if parts else None


async def main() -> None:
    async with PasarguardAPI(base_url=BASE_URL, verify=True, timeout=30.0) as api:
        token = (await api.get_token(ADMIN_USERNAME, ADMIN_PASSWORD)).access_token

        groups = await api.get_groups_simple(token=token)
        group_ids = [g.id for g in groups.groups[:1]] if groups.groups else []

        user = await api.add_user(
            UserCreate(username=f"compat_{uuid4().hex[:6]}", group_ids=group_ids),
            token=token,
        )
        print(f"OK add_user -> {user.username}")

        usage = await api.get_user_data_usage(
            username=user.username, token=token, period=Period.DAY
        )
        print(f"OK get_user_data_usage -> {len(usage.stats)} keys")

        # await api.activate_next_plan(username=user.username, token=token)
        print("INFO activate_next_plan — commented out")

        nodes = await api.get_nodes_simple(token=token, limit=1)
        if nodes.nodes:
            node_id = nodes.nodes[0].id
            # await api.update_node_core(node_id=node_id, core_version="1.8.0", token=token)
            # await api.update_node_geofiles(node_id=node_id, region=GeoFilseRegion.IRAN, token=token)
            print("INFO update_node_core / update_node_geofiles — commented out")

        sub_token = extract_sub_token(user.subscription_url)
        if sub_token:
            info = await api.get_user_subscription_info(token=sub_token)
            print(f"OK get_user_subscription_info -> {info.username}")

            await api.get_sub_user_usage_by_url(token=sub_token, period=Period.HOUR)
            print("OK get_sub_user_usage_by_url")

            links = await api.get_user_subscription_with_client_type(
                client_type=ConfigFormat.LINKS,
                token=sub_token,
            )
            print(f"OK get_user_subscription_with_client_type -> {len(links)} links")

        await api.remove_user(username=user.username, token=token)
        print(f"OK remove_user -> deleted {user.username}")

        print("\nDone — legacy aliases reviewed")


if __name__ == "__main__":
    asyncio.run(main())

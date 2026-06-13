"""
Group management.

Methods covered:
- create_group, get_all_groups, get_groups_simple, get_group
- modify_group, remove_group
- bulk_add_groups_to_users, bulk_remove_users_from_groups
- bulk_delete_groups, bulk_disable_groups, bulk_enable_groups

Run: python groups.py
"""

from __future__ import annotations

import asyncio
import os

from pasarguard import BulkGroup, BulkGroupSelection, PasarguardAPI

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")
ADMIN_USERNAME = os.environ.get("PASARGUARD_ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("PASARGUARD_ADMIN_PASSWORD", "password")


async def main() -> None:
    async with PasarguardAPI(base_url=BASE_URL, verify=True, timeout=30.0) as api:
        token = (await api.get_token(ADMIN_USERNAME, ADMIN_PASSWORD)).access_token

        all_groups = await api.get_all_groups(token=token, limit=10)
        print(f"OK get_all_groups -> {len(all_groups.groups)} of {all_groups.total}")

        simple = await api.get_groups_simple(token=token, limit=10)
        print(f"OK get_groups_simple -> {len(simple.groups)} groups")

        if not simple.groups:
            print("No groups found")
            return

        group_id = simple.groups[0].id
        group = await api.get_group(group_id=group_id, token=token)
        print(f"OK get_group -> {group.name} ({group.total_users} users)")

        # inbounds = await api.get_inbounds(token=token)
        # await api.create_group(
        #     GroupCreate(name="example_group", inbound_tags=inbounds[:1] or ["VLESS TCP"]),
        #     token=token,
        # )
        # await api.modify_group(group_id=group_id, group=GroupModify(name=group.name), token=token)
        # await api.remove_group(group_id=group_id, token=token)

        selection = BulkGroupSelection(ids=[group_id])
        # await api.bulk_disable_groups(selection, token=token)
        # await api.bulk_enable_groups(selection, token=token)
        # await api.bulk_delete_groups(selection, token=token)

        # users = await api.get_users_simple(token=token, limit=1)
        # if users.users:
        #     await api.bulk_add_groups_to_users(
        #         BulkGroup(group_ids=[group_id], users=[users.users[0].id]), token=token
        #     )
        #     await api.bulk_remove_users_from_groups(
        #         BulkGroup(group_ids=[group_id], users=[users.users[0].id]), token=token
        #     )

        print("INFO create/modify/remove/bulk — commented out")
        print("\nDone — groups reviewed")


if __name__ == "__main__":
    asyncio.run(main())

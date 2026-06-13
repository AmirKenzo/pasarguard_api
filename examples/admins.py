"""
Admin management.

Methods covered:
- get_current_admin, create_admin, modify_admin, remove_admin
- get_admins, get_admins_simple
- get_admin_usage (by username / by id)
- disable/activate/remove all users of an admin
- reset_admin_usage
- bulk admin operations

Run: python admins.py
"""

from __future__ import annotations

import asyncio
import os

from pasarguard import PasarguardAPI, Period

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")
ADMIN_USERNAME = os.environ.get("PASARGUARD_ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("PASARGUARD_ADMIN_PASSWORD", "password")


async def main() -> None:
    async with PasarguardAPI(base_url=BASE_URL, verify=True, timeout=30.0) as api:
        token = (await api.get_token(ADMIN_USERNAME, ADMIN_PASSWORD)).access_token

        me = await api.get_current_admin(token=token)
        print(f"OK get_current_admin -> {me.username}")

        admins = await api.get_admins(token=token, limit=10)
        print(f"OK get_admins -> {len(admins.admins)} of {admins.total}")

        simple = await api.get_admins_simple(token=token, limit=5)
        print(f"OK get_admins_simple -> {len(simple.admins)} admins")

        if not admins.admins:
            return

        admin_username = admins.admins[0].username
        admin_id = admins.admins[0].id

        usage = await api.get_admin_usage(
            username=admin_username, token=token, period=Period.DAY
        )
        print(f"OK get_admin_usage -> {len(usage.stats)} keys")

        await api.get_admin_usage_by_id(admin_id=admin_id, token=token, period=Period.HOUR)
        print("OK get_admin_usage_by_id")

        # await api.modify_admin(
        #     username=admin_username,
        #     admin=AdminModify(note="Updated from example"),
        #     token=token,
        # )

        # roles = await api.get_roles_simple(token=token)
        # if roles.roles:
        #     await api.create_admin(
        #         AdminCreate(username="new_admin", password="SecurePass123!", role_id=roles.roles[0].id),
        #         token=token,
        #     )

        # await api.remove_admin(username="new_admin", token=token)
        # await api.reset_admin_usage(username=admin_username, token=token)
        # await api.disable_all_active_users(username=admin_username, token=token)
        # await api.activate_all_disabled_users(username=admin_username, token=token)
        # await api.remove_all_users(username=admin_username, token=token)

        # bulk = BulkAdminSelection(ids=[admin_id])
        # await api.bulk_disable_admins(bulk, token=token)
        # await api.bulk_enable_admins(bulk, token=token)
        # await api.bulk_reset_admins_usage(bulk, token=token)
        # await api.bulk_delete_admins(bulk, token=token)
        # await api.bulk_disable_all_active_users(bulk, token=token)
        # await api.bulk_activate_all_disabled_users(bulk, token=token)
        # await api.bulk_remove_all_users(bulk, token=token)

        print("INFO create/modify/remove/bulk — commented out (destructive)")
        print(f"\nDone — sample admin: {admin_username}")


if __name__ == "__main__":
    asyncio.run(main())

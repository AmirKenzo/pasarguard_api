"""
Admin roles.

Methods covered:
- create_role, get_role, modify_role, delete_role
- get_roles, get_roles_simple

Run: python admin_roles.py
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

        roles = await api.get_roles(token=token)
        print(f"OK get_roles -> {len(roles.roles)} roles")

        simple = await api.get_roles_simple(token=token)
        print(f"OK get_roles_simple -> {len(simple.roles)} roles")

        if roles.roles:
            detail = await api.get_role(role_id=roles.roles[0].id, token=token)
            print(f"OK get_role -> {detail.name}")

        # await api.create_role(AdminRoleCreate(name="example_role", permissions=...), token=token)
        # await api.modify_role(role_id=..., role=AdminRoleModify(name="updated"), token=token)
        # await api.delete_role(role_id=..., token=token)

        print("INFO create/modify/delete — commented out")
        print("\nDone — admin roles reviewed")


if __name__ == "__main__":
    asyncio.run(main())

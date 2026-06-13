"""
User template management.

Methods covered:
- create_user_template, get_user_template, modify_user_template
- remove_user_template, get_user_templates, get_user_templates_simple
- bulk_delete_user_templates, bulk_disable_user_templates, bulk_enable_user_templates

Run: python user_templates.py
"""

from __future__ import annotations

import asyncio
import os

from pasarguard import BulkUserTemplateSelection, PasarguardAPI

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")
ADMIN_USERNAME = os.environ.get("PASARGUARD_ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("PASARGUARD_ADMIN_PASSWORD", "password")


async def main() -> None:
    async with PasarguardAPI(base_url=BASE_URL, verify=True, timeout=30.0) as api:
        token = (await api.get_token(ADMIN_USERNAME, ADMIN_PASSWORD)).access_token

        templates = await api.get_user_templates(token=token, limit=10)
        print(f"OK get_user_templates -> {len(templates)} templates")

        simple = await api.get_user_templates_simple(token=token, limit=10)
        print(f"OK get_user_templates_simple -> {len(simple.templates)} templates")

        if templates:
            tpl_id = templates[0].id
            detail = await api.get_user_template(template_id=tpl_id, token=token)
            print(f"OK get_user_template -> id={detail.id}")

            bulk = BulkUserTemplateSelection(ids=[tpl_id])
            # await api.bulk_disable_user_templates(bulk, token=token)
            # await api.bulk_enable_user_templates(bulk, token=token)
            # await api.bulk_delete_user_templates(bulk, token=token)

        # await api.create_user_template(UserTemplateCreate(...), token=token)
        # await api.modify_user_template(tpl_id, UserTemplateModify(...), token=token)
        # await api.remove_user_template(template_id=tpl_id, token=token)

        print("INFO create/modify/remove/bulk — commented out")
        print("\nDone — user templates reviewed")


if __name__ == "__main__":
    asyncio.run(main())

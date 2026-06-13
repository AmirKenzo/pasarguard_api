"""
Client template management.

Methods covered:
- create_client_template, get_client_template, modify_client_template
- remove_client_template, get_client_templates, get_client_templates_simple
- bulk_delete_client_templates

Run: python client_templates.py
"""

from __future__ import annotations

import asyncio
import os

from pasarguard import BulkClientTemplateSelection, PasarguardAPI

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")
ADMIN_USERNAME = os.environ.get("PASARGUARD_ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("PASARGUARD_ADMIN_PASSWORD", "password")


async def main() -> None:
    async with PasarguardAPI(base_url=BASE_URL, verify=True, timeout=30.0) as api:
        token = (await api.get_token(ADMIN_USERNAME, ADMIN_PASSWORD)).access_token

        templates = await api.get_client_templates(token=token, limit=10)
        tpl_list = templates.templates or []
        print(f"OK get_client_templates -> {len(tpl_list)} templates")

        simple = await api.get_client_templates_simple(token=token, limit=10)
        print(f"OK get_client_templates_simple -> {len(simple.templates)} templates")

        if tpl_list:
            tpl_id = tpl_list[0].id
            detail = await api.get_client_template(template_id=tpl_id, token=token)
            print(f"OK get_client_template -> id={detail.id}")

            bulk = BulkClientTemplateSelection(ids=[tpl_id])
            # await api.bulk_delete_client_templates(bulk, token=token)

        # await api.create_client_template(ClientTemplateCreate(...), token=token)
        # await api.modify_client_template(tpl_id, ClientTemplateModify(...), token=token)
        # await api.remove_client_template(template_id=tpl_id, token=token)

        print("INFO create/modify/remove/bulk — commented out")
        print("\nDone — client templates reviewed")


if __name__ == "__main__":
    asyncio.run(main())

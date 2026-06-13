"""
User management — all UserMixin methods.

Many methods have username / by_username / by_id variants.
This file demonstrates one variant per operation; the others work the same way.

Run: python users.py
"""

from __future__ import annotations

import asyncio
import os
from uuid import uuid4

from pasarguard import (
    ConfigFormat,
    PasarguardAPI,
    Period,
    UserCountMetric,
    UserCreate,
    UserModify,
    UserStatus,
)

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")
ADMIN_USERNAME = os.environ.get("PASARGUARD_ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("PASARGUARD_ADMIN_PASSWORD", "password")


async def demo_crud(api: PasarguardAPI, token: str, username: str, user_id: int) -> None:
    groups = await api.get_groups_simple(token=token)
    group_ids = [g.id for g in groups.groups[:1]] if groups.groups else []

    new_name = f"demo_{uuid4().hex[:6]}"
    created = await api.create_user(
        UserCreate(username=new_name, group_ids=group_ids, note="CRUD demo"),
        token=token,
    )
    print(f"OK create_user -> {created.username}")

    user = await api.get_user(username=username, token=token)
    print(f"OK get_user -> id={user.id}")

    user_by_id = await api.get_user_by_id(user_id=user_id, token=token)
    print(f"OK get_user_by_id -> {user_by_id.username}")

    updated = await api.modify_user(
        username=username,
        user=UserModify(note="Updated from example"),
        token=token,
    )
    print(f"OK modify_user -> note={updated.note}")

    # await api.remove_user(username=new_name, token=token)


async def demo_lists(api: PasarguardAPI, token: str) -> None:
    users = await api.get_users(
        token=token,
        offset=0,
        limit=10,
        status=UserStatus.ACTIVE,
        load_sub=False,
    )
    print(f"OK get_users -> {len(users.users)} of {users.total}")

    simple = await api.get_users_simple(token=token, limit=5)
    print(f"OK get_users_simple -> {len(simple.users)} users")


async def demo_usage(api: PasarguardAPI, token: str, username: str) -> None:
    usage = await api.get_user_usage(username=username, token=token, period=Period.DAY)
    print(f"OK get_user_usage -> {len(usage.stats)} keys")

    all_usage = await api.get_users_usage(token=token, period=Period.HOUR)
    print(f"OK get_users_usage -> {len(all_usage.stats)} keys")

    metric = await api.get_users_count_metric(
        metric=UserCountMetric.ONLINE,
        token=token,
        period=Period.DAY,
    )
    print(f"OK get_users_count_metric -> {len(metric.stats)} keys")


async def demo_subscription_actions(
    api: PasarguardAPI, token: str, username: str, user_id: int
) -> None:
    # await api.reset_user_data_usage(username=username, token=token)
    # await api.revoke_user_subscription(username=username, token=token)
    # await api.active_next_plan(username=username, token=token)

    sub = await api.get_user_subscription_by_id(
        user_id=user_id,
        client_type=ConfigFormat.LINKS,
        token=token,
    )
    print(f"OK get_user_subscription_by_id -> {type(sub).__name__}")

    chart = await api.get_users_sub_update_chart(token=token, username=username)
    print("OK get_users_sub_update_chart")

    updates = await api.get_user_sub_update_list(username=username, token=token, limit=5)
    print(f"OK get_user_sub_update_list -> {updates.count} items")


async def demo_expired(api: PasarguardAPI, token: str) -> None:
    expired = await api.get_expired_users(token=token)
    print(f"OK get_expired_users -> {len(expired)} users")

    # await api.delete_expired_users(token=token)


async def demo_bulk(api: PasarguardAPI, token: str, user_ids: list[int]) -> None:
    if not user_ids:
        print("INFO bulk — no users to demonstrate")
        return

    # selection = BulkUsersSelection(ids=user_ids[:1])

    # await api.bulk_disable_users(selection, token=token)
    # await api.bulk_enable_users(selection, token=token)
    # await api.bulk_reset_users_data_usage(selection, token=token)
    # await api.bulk_revoke_users_subscription(selection, token=token)
    # await api.bulk_delete_users(selection, token=token)
    # await api.bulk_set_owner(BulkUsersSetOwner(ids=user_ids[:1], admin_username="admin"), token=token)
    # await api.bulk_modify_users_expire(BulkUser(users=user_ids[:1], amount=30, dry_run=True), token=token)
    # await api.bulk_modify_users_datalimit(BulkUser(users=user_ids[:1], amount=10 * 1024**3, dry_run=True), token=token)
    # await api.bulk_modify_users_proxy_settings(BulkUsersProxy(users=user_ids[:1], dry_run=True), token=token)
    # await api.bulk_reallocate_wireguard_peer_ips(
    #     BulkWireGuardPeerIPs(users=user_ids[:1], dry_run=True, confirm=False), token=token
    # )

    print("INFO bulk_* methods — commented out (destructive)")


async def demo_templates(
    api: PasarguardAPI, token: str, username: str, user_id: int
) -> None:
    templates = await api.get_user_templates_simple(token=token, limit=1)
    if not templates.templates:
        print("INFO template methods — no user templates found")
        return

    tpl_id = templates.templates[0].id

    # await api.create_user_from_template(
    #     CreateUserFromTemplate(user_template_id=tpl_id, username=f"from_tpl_{uuid4().hex[:6]}"),
    #     token=token,
    # )
    # await api.bulk_create_users_from_template(
    #     BulkUsersFromTemplate(user_template_id=tpl_id, count=1), token=token
    # )
    # await api.modify_user_with_template(
    #     username=username, template_user=ModifyUserByTemplate(user_template_id=tpl_id), token=token
    # )
    # await api.bulk_apply_template_to_users(
    #     BulkUsersApplyTemplate(user_template_id=tpl_id, ids=[user_id]), token=token
    # )

    print("INFO template methods — commented out")


async def main() -> None:
    async with PasarguardAPI(base_url=BASE_URL, verify=True, timeout=30.0) as api:
        token = (await api.get_token(ADMIN_USERNAME, ADMIN_PASSWORD)).access_token

        users = await api.get_users_simple(token=token, limit=1)
        if not users.users:
            print("No users found — run getting_started.py first")
            return

        username = users.users[0].username
        user_id = users.users[0].id
        all_ids = [u.id for u in users.users]

        print(f"Sample user: {username} (id={user_id})\n")

        await demo_lists(api, token)
        await demo_crud(api, token, username, user_id)
        await demo_usage(api, token, username)
        await demo_subscription_actions(api, token, username, user_id)
        await demo_expired(api, token)
        await demo_bulk(api, token, all_ids)
        await demo_templates(api, token, username, user_id)

        # await api.reset_users_data_usage(token=token)
        print("\nDone — all user methods reviewed")


if __name__ == "__main__":
    asyncio.run(main())

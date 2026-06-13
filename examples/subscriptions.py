"""
User subscription endpoints.

Methods covered:
- user_subscription, user_subscription_info, user_subscription_raw
- user_subscription_apps, get_sub_user_usage
- user_subscription_with_client_type
- get_user_subscription_info (compat)
- get_sub_user_usage_by_url (compat)
- get_user_subscription_with_client_type (compat)

Note: these methods use the user's subscription token, not the admin token.
Extract it from subscription_url (e.g. https://panel.example.com/sub/TOKEN/).

Run: python subscriptions.py
"""

from __future__ import annotations

import asyncio
import os

from pasarguard import ConfigFormat, PasarguardAPI, Period

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")
ADMIN_USERNAME = os.environ.get("PASARGUARD_ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("PASARGUARD_ADMIN_PASSWORD", "password")


def extract_sub_token(subscription_url: str | None) -> str | None:
    """Extract subscription token from a subscription URL."""
    if not subscription_url:
        return None
    parts = subscription_url.rstrip("/").split("/")
    if len(parts) >= 2 and parts[-2] == "sub":
        return parts[-1]
    return parts[-1] if parts else None


async def main() -> None:
    async with PasarguardAPI(base_url=BASE_URL, verify=True, timeout=30.0) as api:
        admin_token = (await api.get_token(ADMIN_USERNAME, ADMIN_PASSWORD)).access_token

        users = await api.get_users(token=admin_token, limit=1, load_sub=True)
        if not users.users:
            print("No users found")
            return

        user = users.users[0]
        sub_token = extract_sub_token(user.subscription_url)

        if not sub_token:
            print("User has no subscription URL")
            return

        print(f"User: {user.username}\n")

        info = await api.user_subscription_info(token=sub_token)
        print(f"OK user_subscription_info -> {info.username}")

        info_compat = await api.get_user_subscription_info(token=sub_token)
        print(f"OK get_user_subscription_info (compat) -> {info_compat.username}")

        # info_from_url = await api.get_user_subscription_info(url=user.subscription_url)

        sub = await api.user_subscription(token=sub_token)
        print(f"OK user_subscription -> {type(sub).__name__}")

        await api.user_subscription_raw(token=sub_token)
        print("OK user_subscription_raw")

        apps = await api.user_subscription_apps(token=sub_token)
        print(f"OK user_subscription_apps -> {len(apps)} apps")

        usage = await api.get_sub_user_usage(token=sub_token, period=Period.DAY)
        print(f"OK get_sub_user_usage -> {len(usage.stats)} keys")

        await api.get_sub_user_usage_by_url(token=sub_token, period=Period.HOUR)
        print("OK get_sub_user_usage_by_url (compat)")

        await api.user_subscription_with_client_type(
            token=sub_token, client_type=ConfigFormat.LINKS
        )
        print("OK user_subscription_with_client_type")

        links = await api.get_user_subscription_with_client_type(
            client_type=ConfigFormat.LINKS,
            token=sub_token,
        )
        print(f"OK get_user_subscription_with_client_type (compat) -> {len(links)} links")

        print("\nDone — subscriptions reviewed")


if __name__ == "__main__":
    asyncio.run(main())

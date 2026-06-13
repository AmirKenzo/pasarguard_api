"""
Authentication and token caching.

Methods covered:
- get_token / admin_token
- get_current_admin
- admin_mini_app_token (Telegram Mini App)
- PasarguardTokenCache

Run: python authentication.py
"""

from __future__ import annotations

import asyncio
import os

from pasarguard import PasarguardAPI, PasarguardTokenCache

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")
ADMIN_USERNAME = os.environ.get("PASARGUARD_ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("PASARGUARD_ADMIN_PASSWORD", "password")


async def main() -> None:
    async with PasarguardAPI(base_url=BASE_URL, verify=True, timeout=30.0) as api:
        token = (await api.get_token(ADMIN_USERNAME, ADMIN_PASSWORD)).access_token
        print("OK get_token")

        await api.admin_token(username=ADMIN_USERNAME, password=ADMIN_PASSWORD)
        print("OK admin_token")

        admin = await api.get_current_admin(token=token)
        print(f"OK get_current_admin -> {admin.username}")

        cache = PasarguardTokenCache(
            client=api,
            username=ADMIN_USERNAME,
            password=ADMIN_PASSWORD,
            token_expire_minutes=1440,
        )
        cached = await cache.get_token()
        assert cached == await cache.get_token()
        print("OK PasarguardTokenCache")

        # Telegram Mini App only — requires a valid X-Telegram-Authorization header
        # telegram_auth = "query_id=...&user=...&auth_date=...&hash=..."
        # await api.admin_mini_app_token(x_telegram_authorization=telegram_auth)
        print("INFO admin_mini_app_token — requires Telegram authorization (commented out)")


if __name__ == "__main__":
    asyncio.run(main())

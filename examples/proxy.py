"""
HTTP/SOCKS proxy for API requests.

The client forwards the ``proxy`` argument to httpx for every request,
including token login and admin API calls.

Supported URL formats:
- ``http://127.0.0.1:8080``
- ``http://user:pass@127.0.0.1:8080``
- ``socks5://127.0.0.1:1080``
- ``socks5://user:pass@127.0.0.1:1080``

You can also rely on environment variables when ``trust_env=True`` (default):
``HTTP_PROXY``, ``HTTPS_PROXY``, and ``ALL_PROXY``.

Run: python proxy.py
"""

from __future__ import annotations

import asyncio
import os

from pasarguard import PasarguardAPI

BASE_URL = os.environ.get("PASARGUARD_BASE_URL", "https://your-panel.example.com")
ADMIN_USERNAME = os.environ.get("PASARGUARD_ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("PASARGUARD_ADMIN_PASSWORD", "password")

# Examples:
#   export PASARGUARD_PROXY="http://127.0.0.1:8080"
#   export PASARGUARD_PROXY="socks5://127.0.0.1:1080"
#   export PASARGUARD_PROXY="http://user:pass@proxy.example.com:8080"
PROXY = os.environ.get("PASARGUARD_PROXY", "http://127.0.0.1:8080")


async def with_explicit_proxy() -> None:
    async with PasarguardAPI(
        base_url=BASE_URL,
        verify=True,
        timeout=30.0,
        proxy=PROXY,
        trust_env=False,
    ) as api:
        health = await api.health()
        print("OK explicit proxy ->", health)

        token = (await api.get_token(ADMIN_USERNAME, ADMIN_PASSWORD)).access_token
        admin = await api.get_current_admin(token=token)
        print(f"OK authenticated via proxy -> {admin.username}")


async def with_env_proxy() -> None:
    # Reads HTTP_PROXY / HTTPS_PROXY / ALL_PROXY from the environment.
    async with PasarguardAPI(
        base_url=BASE_URL,
        verify=True,
        timeout=30.0,
        trust_env=True,
    ) as api:
        health = await api.health()
        print("OK env proxy ->", health)


async def main() -> None:
    print(f"Using proxy: {PROXY}")
    await with_explicit_proxy()
    await with_env_proxy()


if __name__ == "__main__":
    asyncio.run(main())

# Pasarguard

![PyPI](https://img.shields.io/pypi/v/pasarguard?color=blue)
![Python](https://img.shields.io/pypi/pyversions/pasarguard)
![License](https://img.shields.io/pypi/l/pasarguard)
![HTTPX](https://img.shields.io/badge/HTTPX-async-06b6d4)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-ef476f)

**Pasarguard** is a modern, typed, async Python client for the [PasarGuard Panel](https://github.com/PasarGuard/panel) API.

[فارسی](README.fa.md)

It provides a clean interface for authentication, users, admins, nodes, groups, hosts, templates, subscriptions, settings, system stats, and bulk operations. The client is powered by `httpx.AsyncClient` and Pydantic v2 models.

## Installation

```bash
pip install pasarguard
```

```bash
uv add pasarguard
```

## Features

- Async-first API client.
- Typed request and response models with Pydantic v2.
- Bearer-token authentication.
- Optional SSH tunnel support.
- User, admin, node, group, host, core, template, and subscription management.
- Bulk operations for users, admins, nodes, groups, hosts, and templates.
- Usage metrics, realtime node stats, inbound details, and worker health endpoints.

## Compatibility

- Python `>=3.10,<3.15`
- Windows, macOS, and Linux
- `httpx>=0.28.1`
- `pydantic>=2.4.1,<2.13`

## Quick Start

```python
import asyncio
import os

from pasarguard import PasarguardAPI, Tools, UserCreate, UserStatus


async def main() -> None:
    async with PasarguardAPI(
        base_url=os.environ["PASARGUARD_BASE_URL"],
        verify=True,
        timeout=20.0,
    ) as api:
        token = await api.get_token(
            username=os.environ["PASARGUARD_ADMIN_USERNAME"],
            password=os.environ["PASARGUARD_ADMIN_PASSWORD"],
        )

        user = await api.create_user_in_all_groups(
            UserCreate(
                username=Tools.random_username(prefix="customer"),
                data_limit=Tools.gb(50),
                expire=Tools.days(30),
                status=UserStatus.ACTIVE,
                note="Created by automation",
            ),
            token=token.access_token,
        )

        print(user.id, user.username, user.subscription_url)


asyncio.run(main())
```

## Convenience helpers

```python
from pasarguard import Tools

username = Tools.random_username(prefix="trial")
traffic_limit = Tools.gb(20)          # 20 GiB in bytes
expire_at = Tools.days(30)            # Unix timestamp for 30 days from now

assert Tools.to_bytes("500MB") == 500 * 1024**2
assert Tools.to_timestamp("12h") > 0
```

Supported size helpers: `Tools.mb()`, `Tools.gb()`, `Tools.tb()`.
Supported timestamp helpers: `Tools.minutes()`, `Tools.hours()`, `Tools.days()`, `Tools.to_timestamp()`.

## Authentication

```python
token = await api.get_token(
    username=os.environ["PASARGUARD_ADMIN_USERNAME"],
    password=os.environ["PASARGUARD_ADMIN_PASSWORD"],
)

admin = await api.get_current_admin(token=token.access_token)
print(admin.username, admin.is_sudo)
```

`admin_token()` is also available as an alias for `get_token()`.

## Client Initialization

Basic client:

```python
api = PasarguardAPI(
    base_url=os.environ["PASARGUARD_BASE_URL"],
    timeout=10.0,
    verify=True,
)
```

With an SSH tunnel:

```python
api = PasarguardAPI(
    base_url="http://127.0.0.1:8000",
    ssh_host=os.environ["PASARGUARD_SSH_HOST"],
    ssh_username=os.environ["PASARGUARD_SSH_USERNAME"],
    ssh_private_key_path=os.environ["PASARGUARD_SSH_KEY_PATH"],
    local_bind_host="127.0.0.1",
    local_bind_port=8000,
    remote_bind_host="127.0.0.1",
    remote_bind_port=8000,
)
```

## Common Usage

### List Users

```python
from pasarguard import UserStatus

users = await api.get_users(
    token=token,
    offset=0,
    limit=50,
    status=UserStatus.ACTIVE,
    load_sub=True,
)

for user in users.users:
    print(user.username, user.used_traffic)
```

### Modify a User

```python
from pasarguard import UserModify

user = await api.modify_user(
    username="customer-1001",
    user=UserModify(note="Renewed monthly plan"),
    token=token,
)
```

### Bulk Disable Users

```python
from pasarguard import BulkUsersSelection

result = await api.bulk_disable_users(
    BulkUsersSelection(ids=[101, 102, 103]),
    token=token,
)

print(result.count, result.users)
```

### Subscription Info

```python
from pasarguard import ConfigFormat

info = await api.user_subscription_info(token="subscription-token-value")
links = await api.get_user_subscription_with_client_type(
    token="subscription-token-value",
    client_type=ConfigFormat.LINKS,
)

print(info.username)
print("\n".join(links))
```

### Node Stats

```python
stats = await api.realtime_node_stats(node_id=1, token=token)
print(stats.cpu_usage, stats.mem_used)
```

## Error Handling

Pasarguard uses `httpx` internally. HTTP errors are raised as `httpx.HTTPStatusError`.

```python
import httpx

try:
    user = await api.get_user("customer-1001", token=token)
except httpx.HTTPStatusError as exc:
    print(exc.response.status_code)
    print(exc.response.text)
except httpx.RequestError as exc:
    print(f"Network error: {exc}")
```

## Pagination

Endpoints that return lists commonly support `offset` and `limit`.

```python
offset = 0
limit = 100

while True:
    page = await api.get_users(token=token, offset=offset, limit=limit)

    for user in page.users:
        print(user.username)

    offset += limit
    if offset >= page.total:
        break
```

## API Overview

Main public client: `PasarguardAPI`

Important method groups:

- Authentication: `get_token()`, `admin_token()`
- Users: `create_user()`, `get_user()`, `get_users()`, `modify_user()`, `remove_user()`
- User bulk actions: `bulk_delete_users()`, `bulk_disable_users()`, `bulk_enable_users()`, `bulk_reset_users_data_usage()`
- Admins: `get_current_admin()`, `create_admin()`, `get_admins()`, `modify_admin()`, `remove_admin()`
- Nodes: `create_node()`, `get_nodes()`, `realtime_node_stats()`, `sync_node()`, `reconnect_node()`
- Groups: `create_group()`, `get_all_groups()`, `modify_group()`, `remove_group()`
- Hosts: `create_host()`, `get_hosts()`, `modify_host()`, `remove_host()`
- Cores: `create_core_config()`, `get_all_cores()`, `restart_core()`
- Templates: `create_user_template()`, `create_client_template()`
- Subscriptions: `user_subscription_info()`, `user_subscription_with_client_type()`
- Settings and system: `get_settings()`, `modify_settings()`, `get_system_stats()`, `get_workers_health()`

Common public models:

- `UserCreate`, `UserModify`, `UserResponse`, `UsersResponse`
- `AdminCreate`, `AdminModify`, `AdminDetails`
- `NodeCreate`, `NodeModify`, `NodeResponse`
- `GroupCreate`, `GroupModify`, `GroupResponse`
- `CreateHost`, `BaseHost`
- `CoreCreate`, `CoreResponse`
- `SettingsSchema`, `SubscriptionUserResponse`

Common enums:

- `UserStatus`
- `Period`
- `ConfigFormat`
- `DataLimitResetStrategy`
- `NodeStatus`
- `NodeConnectionType`
- `CoreType`

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

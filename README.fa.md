# پاسارگارد

![PyPI](https://img.shields.io/pypi/v/pasarguard?color=blue)
![Python](https://img.shields.io/pypi/pyversions/pasarguard)
![License](https://img.shields.io/pypi/l/pasarguard)
![HTTPX](https://img.shields.io/badge/HTTPX-async-06b6d4)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-ef476f)

<div dir="rtl">

**Pasarguard** یک کلاینت مدرن، تایپ‌شده و غیرهمزمان برای کار با API [پنل PasarGuard](https://github.com/PasarGuard/panel) در پایتون است.

[English](README.md)

این کتابخانه برای احراز هویت، مدیریت کاربران، ادمین‌ها، نودها، گروه‌ها، هاست‌ها، قالب‌ها، اشتراک‌ها، تنظیمات، آمار سیستم و عملیات گروهی طراحی شده است. کلاینت بر پایه‌ی `httpx.AsyncClient` و مدل‌های Pydantic v2 ساخته شده است.

## نصب

```bash
pip install pasarguard
```

```bash
uv add pasarguard
```

## قابلیت‌ها

- کلاینت کاملاً async.
- مدل‌های تایپ‌شده برای درخواست و پاسخ با Pydantic v2.
- احراز هویت با Bearer Token.
- پشتیبانی اختیاری از تونل SSH.
- مدیریت کاربران، ادمین‌ها، نودها، گروه‌ها، هاست‌ها، coreها، قالب‌ها و اشتراک‌ها.
- عملیات گروهی برای کاربران، ادمین‌ها، نودها، گروه‌ها، هاست‌ها و قالب‌ها.
- دریافت آمار مصرف، وضعیت لحظه‌ای نودها، جزئیات inbound و سلامت workerها.

## سازگاری

- پایتون `>=3.10,<3.15`
- ویندوز، مک‌اواس و لینوکس
- `httpx>=0.28.1`
- `pydantic>=2.4.1,<2.13`

## شروع سریع

</div>

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

<div dir="rtl">

## ابزارهای کمکی

</div>

```python
from pasarguard import Tools

username = Tools.random_username(prefix="trial")
traffic_limit = Tools.gb(20)          # 20 GiB in bytes
expire_at = Tools.days(30)            # Unix timestamp for 30 days from now

assert Tools.to_bytes("500MB") == 500 * 1024**2
assert Tools.to_timestamp("12h") > 0
```

<div dir="rtl">

ابزارهای حجم پشتیبانی‌شده: `Tools.mb()`، `Tools.gb()` و `Tools.tb()`.
ابزارهای زمان، timestamp آینده برمی‌گردانند: `Tools.minutes()`، `Tools.hours()`، `Tools.days()` و `Tools.to_timestamp()`.

</div>

<div dir="rtl">

## احراز هویت

</div>

```python
token = await api.get_token(
    username=os.environ["PASARGUARD_ADMIN_USERNAME"],
    password=os.environ["PASARGUARD_ADMIN_PASSWORD"],
)

admin = await api.get_current_admin(token=token.access_token)
print(admin.username, admin.is_sudo)
```

<div dir="rtl">

متد `admin_token()` نیز به عنوان نام جایگزین برای `get_token()` وجود دارد.

## ساخت کلاینت

نمونه ساده:

</div>

```python
api = PasarguardAPI(
    base_url=os.environ["PASARGUARD_BASE_URL"],
    timeout=10.0,
    verify=True,
)
```

<div dir="rtl">

با تونل SSH:

</div>

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

<div dir="rtl">

## نمونه‌های رایج

### دریافت لیست کاربران

</div>

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

<div dir="rtl">

### تغییر کاربر

</div>

```python
from pasarguard import UserModify

user = await api.modify_user(
    username="customer-1001",
    user=UserModify(note="Renewed monthly plan"),
    token=token,
)
```

<div dir="rtl">

### غیرفعال‌سازی گروهی کاربران

</div>

```python
from pasarguard import BulkUsersSelection

result = await api.bulk_disable_users(
    BulkUsersSelection(ids=[101, 102, 103]),
    token=token,
)

print(result.count, result.users)
```

<div dir="rtl">

### اطلاعات اشتراک

</div>

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

<div dir="rtl">

### آمار لحظه‌ای نود

</div>

```python
stats = await api.realtime_node_stats(node_id=1, token=token)
print(stats.cpu_usage, stats.mem_used)
```

<div dir="rtl">

## مدیریت خطا

Pasarguard در داخل از `httpx` استفاده می‌کند. خطاهای HTTP به صورت `httpx.HTTPStatusError` ایجاد می‌شوند.

</div>

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

<div dir="rtl">

## صفحه‌بندی

endpointهایی که لیست برمی‌گردانند معمولاً از `offset` و `limit` پشتیبانی می‌کنند.

</div>

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

<div dir="rtl">

## مرور API

کلاینت اصلی: `PasarguardAPI`

گروه‌های مهم متدها:

- احراز هویت: `get_token()` و `admin_token()`
- کاربران: `create_user()`، `get_user()`، `get_users()`، `modify_user()` و `remove_user()`
- عملیات گروهی کاربران: `bulk_delete_users()`، `bulk_disable_users()`، `bulk_enable_users()` و `bulk_reset_users_data_usage()`
- ادمین‌ها: `get_current_admin()`، `create_admin()`، `get_admins()`، `modify_admin()` و `remove_admin()`
- نودها: `create_node()`، `get_nodes()`، `realtime_node_stats()`، `sync_node()` و `reconnect_node()`
- گروه‌ها: `create_group()`، `get_all_groups()`، `modify_group()` و `remove_group()`
- هاست‌ها: `create_host()`، `get_hosts()`، `modify_host()` و `remove_host()`
- coreها: `create_core_config()`، `get_all_cores()` و `restart_core()`
- قالب‌ها: `create_user_template()` و `create_client_template()`
- اشتراک‌ها: `user_subscription_info()` و `user_subscription_with_client_type()`
- تنظیمات و سیستم: `get_settings()`، `modify_settings()`، `get_system_stats()` و `get_workers_health()`

مدل‌های پرکاربرد:

- `UserCreate`، `UserModify`، `UserResponse`، `UsersResponse`
- `AdminCreate`، `AdminModify`، `AdminDetails`
- `NodeCreate`، `NodeModify`، `NodeResponse`
- `GroupCreate`، `GroupModify`، `GroupResponse`
- `CreateHost`، `BaseHost`
- `CoreCreate`، `CoreResponse`
- `SettingsSchema`، `SubscriptionUserResponse`

Enumهای پرکاربرد:

- `UserStatus`
- `Period`
- `ConfigFormat`
- `DataLimitResetStrategy`
- `NodeStatus`
- `NodeConnectionType`
- `CoreType`

## مجوز

این پروژه تحت مجوز MIT منتشر شده است. برای جزئیات فایل [LICENSE](LICENSE) را ببینید.

</div>

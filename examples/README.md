# Pasarguard SDK Examples

Practical examples for every `PasarguardAPI` method. Each file is standalone — copy it, set your credentials, and run.

## Install

```bash
pip install pasarguard
```

## Configuration

Set environment variables before running:

```bash
export PASARGUARD_BASE_URL="https://panel.example.com"
export PASARGUARD_ADMIN_USERNAME="admin"
export PASARGUARD_ADMIN_PASSWORD="your-password"
export PASARGUARD_API_KEY="pg_key_..."   # optional: skip login, use API key auth
```

PowerShell:

```powershell
$env:PASARGUARD_BASE_URL="https://panel.example.com"
$env:PASARGUARD_ADMIN_USERNAME="admin"
$env:PASARGUARD_ADMIN_PASSWORD="your-password"
```

Or edit the `BASE_URL`, `ADMIN_USERNAME`, and `ADMIN_PASSWORD` constants at the top of each file.

## Run an example

```bash
python getting_started.py
python tools.py
python users.py
```

## Files

| File | Topic |
|------|--------|
| [`getting_started.py`](getting_started.py) | Client setup, token, create user |
| [`tools.py`](tools.py) | SDK tools for sizes, durations, usernames, and all-group user creation |
| [`authentication.py`](authentication.py) | Auth, token cache, current admin |
| [`users.py`](users.py) | User CRUD, bulk ops, templates, usage |
| [`admins.py`](admins.py) | Admin management |
| [`admin_roles.py`](admin_roles.py) | Admin roles |
| [`api_keys.py`](api_keys.py) | API keys (create, list, revoke, delete) |
| [`groups.py`](groups.py) | Groups |
| [`nodes.py`](nodes.py) | Nodes, stats, sync |
| [`hosts.py`](hosts.py) | Hosts |
| [`cores.py`](cores.py) | Core configs |
| [`client_templates.py`](client_templates.py) | Client templates |
| [`user_templates.py`](user_templates.py) | User templates |
| [`subscriptions.py`](subscriptions.py) | User subscription endpoints |
| [`settings.py`](settings.py) | Panel settings |
| [`system.py`](system.py) | System stats and inbounds |
| [`setup.py`](setup.py) | Initial owner setup |
| [`user_hwid.py`](user_hwid.py) | User HWID devices |
| [`health.py`](health.py) | API health |
| [`proxy.py`](proxy.py) | HTTP/SOCKS proxy for API requests |
| [`legacy_aliases.py`](legacy_aliases.py) | Backward-compatible method names |

## Notes

1. Pass `token.access_token` from `get_token()` to authenticated methods.
2. Prefer `async with PasarguardAPI(...) as api:` so connections close cleanly.
3. Destructive calls (delete, bulk delete, global reset) are commented out by default.
4. Use `dry_run=True` on bulk modify payloads to preview changes without applying them.
5. HTTP errors raise `httpx.HTTPStatusError`.

## Duplicate method variants

Many methods exist in three forms: by username, `*_by_username`, and `*_by_id`. Examples usually show one variant; the others behave the same aside from the identifier type.

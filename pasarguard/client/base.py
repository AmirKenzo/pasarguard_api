from __future__ import annotations

# ruff: noqa: F401, F403
from ._imports import *


class BaseAPIClient:
    def __init__(
        self,
        base_url: str,
        *,
        timeout: float = 10.0,
        verify: bool = False,
        ssh_username: Optional[str] = None,
        ssh_host: Optional[str] = None,
        ssh_port: Optional[int] = 22,
        ssh_private_key_path: Optional[str] = None,
        ssh_key_passphrase: Optional[str] = None,
        ssh_password: Optional[str] = None,
        local_bind_host: str = "127.0.0.1",
        local_bind_port: int = 8000,
        remote_bind_host: str = "127.0.0.1",
        remote_bind_port: int = 8000,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.verify = verify
        self.ssh_username = ssh_username
        self.ssh_host = ssh_host
        self.ssh_port = ssh_port
        self.ssh_private_key_path = ssh_private_key_path
        self.ssh_key_passphrase = ssh_key_passphrase
        self.ssh_password = ssh_password
        self.local_bind_host = local_bind_host
        self.local_bind_port = local_bind_port
        self.remote_bind_host = remote_bind_host
        self.remote_bind_port = remote_bind_port
        self.client: Optional[httpx.AsyncClient] = None
        self._tunnel = None
        if ssh_host and not ssh_private_key_path and not ssh_password:
            raise ValueError("For an SSH tunnel, specify either ssh_private_key_path or ssh_password")
        if not ssh_host:
            self.client = httpx.AsyncClient(base_url=self.base_url, verify=self.verify, timeout=self.timeout)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    def _load_private_key(self, key_path: str, passphrase: Optional[str]):
        for key_class in (paramiko.RSAKey, paramiko.DSSKey, paramiko.ECDSAKey, paramiko.Ed25519Key):
            try:
                return key_class.from_private_key_file(key_path, password=passphrase)
            except paramiko.ssh_exception.PasswordRequiredException:
                raise ValueError("Private key is encrypted; provide ssh_key_passphrase") from None
            except SSHException:
                continue
        raise ValueError("Unsupported key format or incorrect passphrase")

    def _initialize(self) -> None:
        if not self.ssh_host:
            return
        if self._tunnel and self._tunnel.is_active:
            return
        private_key = self._load_private_key(self.ssh_private_key_path, self.ssh_key_passphrase) if self.ssh_private_key_path else None
        self._tunnel = SSHTunnelForwarder(
            (self.ssh_host, self.ssh_port),
            ssh_username=self.ssh_username,
            ssh_password=self.ssh_password,
            ssh_pkey=private_key,
            remote_bind_address=(self.remote_bind_host, self.remote_bind_port),
            local_bind_address=(self.local_bind_host, self.local_bind_port),
        )
        self._tunnel.start()
        self.client = httpx.AsyncClient(
            base_url=f"http://{self.local_bind_host}:{self.local_bind_port}",
            timeout=self.timeout,
            verify=self.verify,
        )

    def _ensure_client(self) -> httpx.AsyncClient:
        if self.ssh_host and (not self.client or not self._tunnel or not self._tunnel.is_active):
            self._initialize()
        if not self.client:
            self.client = httpx.AsyncClient(base_url=self.base_url, verify=self.verify, timeout=self.timeout)
        return self.client

    def _get_headers(self, token: Optional[str] = None, extra: Optional[Mapping[str, Any]] = None) -> Dict[str, str]:
        headers: Dict[str, str] = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        for key, value in (extra or {}).items():
            if value is not None:
                headers[key] = str(self._serialize(value))
        return headers

    def _serialize(self, value: Any) -> Any:
        if isinstance(value, BaseModel):
            return value.model_dump(mode="json", by_alias=True, exclude_none=True, exclude_unset=True)
        if isinstance(value, Enum):
            return value.value
        if isinstance(value, (datetime, date)):
            return value.isoformat()
        if isinstance(value, list):
            return [self._serialize(item) for item in value]
        if isinstance(value, tuple):
            return [self._serialize(item) for item in value]
        if isinstance(value, dict):
            return {key: self._serialize(item) for key, item in value.items() if item is not None}
        return value

    def _clean_params(self, params: Optional[Mapping[str, Any]]) -> Dict[str, Any]:
        return {key: self._serialize(value) for key, value in (params or {}).items() if value is not None}

    def _validate_payload(self, data: Any, model: Any) -> Any:
        if data is None:
            return None
        validated = TypeAdapter(model).validate_python(data)
        return self._serialize(validated)

    async def _request(
        self,
        method: str,
        url: str,
        *,
        token: Optional[str] = None,
        json_data: Any = None,
        form_data: Any = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, Any]] = None,
    ) -> httpx.Response:
        client = self._ensure_client()
        response = await client.request(
            method,
            url,
            headers=self._get_headers(token, headers),
            json=json_data,
            data=form_data,
            params=self._clean_params(params),
        )
        response.raise_for_status()
        return response

    def _parse_response(self, response: httpx.Response, model: Any) -> Any:
        if model is None or model is type(None):
            return None
        if model is str:
            return response.text
        if not response.content:
            return None
        try:
            payload = response.json()
        except ValueError:
            return response.text
        if model is Any:
            return payload
        return TypeAdapter(model).validate_python(payload)

    async def get_token(self, username: str, password: str) -> Token:
        payload = {"grant_type": "password", "username": username, "password": password, "scope": "", "client_id": "", "client_secret": ""}
        response = await self._request("POST", "/api/admin/token", form_data=payload)
        return self._parse_response(response, Token)

    async def admin_token(self, username: str, password: str) -> Token:
        return await self.get_token(username=username, password=password)

    async def close(self) -> None:
        if self.client:
            await self.client.aclose()
            self.client = None
        if self._tunnel:
            self._tunnel.stop()
            self._tunnel = None

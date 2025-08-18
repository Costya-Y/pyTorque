from __future__ import annotations

import httpx
from typing import Any, Dict, Iterable, List, Optional

from .config import TorqueConfig
from .exceptions import (
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ServerError,
    TorqueError,
)
from .models.environment import Environment, Blueprint

class _BaseClient:
    def __init__(self, config: Optional[TorqueConfig] = None, **overrides):
        self.config = config or TorqueConfig.from_env(**overrides)

    def _handle_response(self, resp: httpx.Response) -> Any:
        if resp.status_code == 401:
            raise AuthenticationError("Unauthorized – check API token")
        if resp.status_code == 404:
            raise NotFoundError("Resource not found")
        if resp.status_code == 429:
            raise RateLimitError("Rate limit exceeded")
        if 500 <= resp.status_code:
            raise ServerError(f"Server error {resp.status_code}: {resp.text}")
        try:
            return resp.json()
        except ValueError:
            raise TorqueError("Invalid JSON response")

    @property
    def base_url(self) -> str:
        return self.config.base_url.rstrip('/')

class TorqueClient(_BaseClient):
    def __enter__(self):
        self._client = httpx.Client(base_url=self.base_url, headers=self.config.headers(), timeout=self.config.timeout, verify=self.config.verify_ssl)
        return self

    def __exit__(self, exc_type, exc, tb):
        if hasattr(self, '_client'):
            self._client.close()

    @property
    def client(self) -> httpx.Client:
        if not hasattr(self, '_client'):
            self._client = httpx.Client(base_url=self.base_url, headers=self.config.headers(), timeout=self.config.timeout, verify=self.config.verify_ssl)
        return self._client

    # Blueprint operations
    def list_blueprints(self) -> List[Blueprint]:
        data = self._handle_response(self.client.get("/blueprints"))
        return [Blueprint(**bp) for bp in data]

    # Environment operations
    def list_environments(self) -> List[Environment]:
        data = self._handle_response(self.client.get("/environments"))
        return [Environment(**env) for env in data]

    def get_environment(self, env_id: str) -> Environment:
        data = self._handle_response(self.client.get(f"/environments/{env_id}"))
        return Environment(**data)

    def launch_environment(self, blueprint_id: str, name: Optional[str] = None, inputs: Optional[Dict[str, Any]] = None) -> Environment:
        payload: Dict[str, Any] = {"blueprint_id": blueprint_id}
        if name:
            payload["name"] = name
        if inputs:
            payload["inputs"] = inputs
        data = self._handle_response(self.client.post("/environments", json=payload))
        return Environment(**data)

    def stop_environment(self, env_id: str) -> Dict[str, Any]:
        return self._handle_response(self.client.post(f"/environments/{env_id}/stop"))

class AsyncTorqueClient(_BaseClient):
    def __init__(self, config: Optional[TorqueConfig] = None, **overrides):
        super().__init__(config, **overrides)
        self._client: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        self._client = httpx.AsyncClient(base_url=self.base_url, headers=self.config.headers(), timeout=self.config.timeout, verify=self.config.verify_ssl)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self._client:
            await self._client.aclose()

    @property
    def client(self) -> httpx.AsyncClient:
        if not self._client:
            self._client = httpx.AsyncClient(base_url=self.base_url, headers=self.config.headers(), timeout=self.config.timeout, verify=self.config.verify_ssl)
        return self._client

    async def list_blueprints(self) -> List[Blueprint]:
        resp = await self.client.get("/blueprints")
        data = self._handle_response(resp)
        return [Blueprint(**bp) for bp in data]

    async def list_environments(self) -> List[Environment]:
        resp = await self.client.get("/environments")
        data = self._handle_response(resp)
        return [Environment(**env) for env in data]

    async def get_environment(self, env_id: str) -> Environment:
        resp = await self.client.get(f"/environments/{env_id}")
        data = self._handle_response(resp)
        return Environment(**data)

    async def launch_environment(self, blueprint_id: str, name: Optional[str] = None, inputs: Optional[Dict[str, Any]] = None) -> Environment:
        payload: Dict[str, Any] = {"blueprint_id": blueprint_id}
        if name:
            payload["name"] = name
        if inputs:
            payload["inputs"] = inputs
        resp = await self.client.post("/environments", json=payload)
        data = self._handle_response(resp)
        return Environment(**data)

    async def stop_environment(self, env_id: str) -> Dict[str, Any]:
        resp = await self.client.post(f"/environments/{env_id}/stop")
        return self._handle_response(resp)

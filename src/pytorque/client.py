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
from .endpoints import TorqueEndpointsMixin, AsyncTorqueEndpointsMixin

class _BaseClient:
    """Internal base for sync & async clients.

    Handles configuration, header (auth) injection and response error mapping.
    """

    def __init__(self, config: Optional[TorqueConfig] = None, **overrides):
        self.config = config or TorqueConfig.from_env(**overrides)
        # underlying httpx client objects created lazily
        self._client: Optional[httpx.Client] = None

    # -------- Authentication helpers ---------
    def ensure_auth(self):
        """Validate that an API token is available, else raise.

        The Bearer token is attached via headers() each time a client is created.
        """
        if not self.config.api_token:
            raise AuthenticationError("Missing API token. Provide via TorqueConfig(api_token=...) or TORQUE_API_TOKEN env var.")

    def set_token(self, token: str):
        """Return a new config with updated token and refresh clients.

        httpx Clients are re-created to pick up new headers.
        """
        from .config import TorqueConfig as _Cfg  # local import to avoid cycles in type checking
        self.config = _Cfg(
            base_url=self.config.base_url,
            api_token=token,
            timeout=self.config.timeout,
            verify_ssl=self.config.verify_ssl,
        )
        # Recreate client(s) so new Authorization header is present
        if self._client:
            try:
                self._client.close()
            except Exception:
                pass
            self._client = None
        if hasattr(self, "_async_client") and getattr(self, "_async_client"):
            # Cannot close here synchronously if still open; user should recreate async client context
            self._async_client = None  # type: ignore[attr-defined]

    # -------- Response handling ---------
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

    def _build_sync_client(self) -> httpx.Client:
        self.ensure_auth()
        return httpx.Client(
            base_url=self.base_url,
            headers=self.config.headers(),
            timeout=self.config.timeout,
            verify=self.config.verify_ssl,
        )

    @property
    def client(self) -> httpx.Client:
        """Sync httpx client (lazily created). Exposed for endpoint mixins."""
        if self._client is None:
            self._client = self._build_sync_client()
        return self._client

class TorqueClient(_BaseClient, TorqueEndpointsMixin):
    """Synchronous Torque API client.

    Provides generated low-level endpoint wrappers (see TorqueEndpointsMixin) plus
    a few convenience methods compatible with earlier simple version of this lib.
    """

    def __enter__(self):  # context manager builds client early
        _ = self.client
        return self

    def __exit__(self, exc_type, exc, tb):
        if self._client:
            self._client.close()

    # Backward compatibility alias
    @property
    def torque_client(self) -> httpx.Client:  # pragma: no cover - simple alias
        return self.client

    # ---- Convenience high-level methods (space-less legacy) ----
    def list_blueprints(self, space_name: Optional[str] = None) -> List[Blueprint]:
        """List blueprints.

        If space_name is provided, uses the official space-scoped endpoint.
        Otherwise attempts legacy /blueprints path (may not exist in all deployments).
        """
        if space_name:
            data = self.get_spaces_by_space_name_blueprints(space_name)  # type: ignore[attr-defined]
        else:
            resp = self.client.get("/blueprints")
            data = self._handle_response(resp)
        data = data or []
        return [Blueprint(**bp) for bp in data if isinstance(bp, dict)]

    def list_environments(self, space_name: Optional[str] = None) -> List[Environment]:
        if space_name:
            # /operation_hub gives global listing; leaving space filter to server if provided elsewhere
            data = self.get_operation_hub(active_only=False)  # type: ignore[attr-defined]
            # Response shape may differ; attempt to extract list heuristically
            if isinstance(data, dict) and "environments" in data:
                items = data["environments"]
            else:
                items = data
        else:
            resp = self.client.get("/environments")
            items = self._handle_response(resp)
        items = items or []
        envs: List[Environment] = []
        for raw in items:
            try:
                envs.append(Environment(**raw))
            except Exception:
                # skip malformed entries silently for now
                continue
        return envs

    def get_environment(self, env_id: str) -> Environment:
        resp = self.client.get(f"/environments/{env_id}")
        data = self._handle_response(resp)
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

class AsyncTorqueClient(_BaseClient, AsyncTorqueEndpointsMixin):
    def __init__(self, config: Optional[TorqueConfig] = None, **overrides):
        super().__init__(config, **overrides)
        self._async_client: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        _ = self.client_async
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self._async_client:
            await self._async_client.aclose()

    def _build_async_client(self) -> httpx.AsyncClient:
        self.ensure_auth()
        return httpx.AsyncClient(
            base_url=self.base_url,
            headers=self.config.headers(),
            timeout=self.config.timeout,
            verify=self.config.verify_ssl,
        )

    @property
    def client_async(self) -> httpx.AsyncClient:
        if self._async_client is None:
            self._async_client = self._build_async_client()
        return self._async_client

    # Expose attribute name expected by endpoint mixin (client)
    @property
    def client(self) -> httpx.AsyncClient:  # type: ignore[override]
        return self.client_async

    # Backward compatibility alias
    @property
    def torque_client(self) -> httpx.AsyncClient:  # pragma: no cover - simple alias
        return self.client_async

    # ---- Async convenience wrappers (legacy) ----
    async def list_blueprints(self, space_name: Optional[str] = None) -> List[Blueprint]:
        if space_name:
            data = await self.get_spaces_by_space_name_blueprints(space_name)  # type: ignore[attr-defined]
        else:
            resp = await self.client.get("/blueprints")
            data = self._handle_response(resp)
        data = data or []
        return [Blueprint(**bp) for bp in data if isinstance(bp, dict)]

    async def list_environments(self, space_name: Optional[str] = None) -> List[Environment]:
        if space_name:
            data = await self.get_operation_hub(active_only=False)  # type: ignore[attr-defined]
            if isinstance(data, dict) and "environments" in data:
                items = data["environments"]
            else:
                items = data
        else:
            resp = await self.client.get("/environments")
            items = self._handle_response(resp)
        items = items or []
        envs: List[Environment] = []
        for raw in items:
            try:
                envs.append(Environment(**raw))
            except Exception:
                continue
        return envs

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

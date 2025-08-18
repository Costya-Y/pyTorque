from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional

DEFAULT_BASE_URL = "https://portal.qtorque.io/api"
TOKEN_ENV_VAR = "TORQUE_API_TOKEN"
BASE_URL_ENV_VAR = "TORQUE_BASE_URL"
USER_AGENT = "pyTorque/0.1.0"

@dataclass(frozen=True)
class TorqueConfig:
    base_url: str = DEFAULT_BASE_URL
    api_token: Optional[str] = None
    timeout: float = 30.0
    verify_ssl: bool = True

    @staticmethod
    def from_env(**overrides) -> "TorqueConfig":
        base_url = overrides.get("base_url") or os.getenv(BASE_URL_ENV_VAR, DEFAULT_BASE_URL)
        api_token = overrides.get("api_token") or os.getenv(TOKEN_ENV_VAR)
        timeout = overrides.get("timeout", 30.0)
        verify_ssl = overrides.get("verify_ssl", True)
        return TorqueConfig(base_url=base_url, api_token=api_token, timeout=timeout, verify_ssl=verify_ssl)

    def headers(self) -> dict:
        hdrs = {"User-Agent": USER_AGENT, "Accept": "application/json"}
        if self.api_token:
            hdrs["Authorization"] = f"Bearer {self.api_token}"
        return hdrs

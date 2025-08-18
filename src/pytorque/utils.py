from __future__ import annotations

import time
from typing import Callable, Optional, Any
from .client import TorqueClient
from .models.environment import Environment, EnvironmentStatus

DEFAULT_POLL_INTERVAL = 5

class EnvironmentWaiter:
    def __init__(self, client: TorqueClient, environment_id: str):
        self.client = client
        self.environment_id = environment_id

    def wait_for_status(self, desired: EnvironmentStatus, timeout: int = 600, interval: int = DEFAULT_POLL_INTERVAL) -> Environment:
        start = time.time()
        while True:
            env = self.client.get_environment(self.environment_id)
            if env.status == desired:
                return env
            if time.time() - start > timeout:
                raise TimeoutError(f"Timed out waiting for status {desired}")
            time.sleep(interval)

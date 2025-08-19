from __future__ import annotations

import time
from typing import Optional

from pytorque.models.generated import EnvironmentResponse
from .client import TorqueClient
from .models.environment import EnvironmentStatus

DEFAULT_POLL_INTERVAL = 5

PHASE_MAP = {
    EnvironmentStatus.PENDING: 'Pending',
    EnvironmentStatus.STARTING: 'Deploying',
    EnvironmentStatus.RUNNING: 'Active',
    EnvironmentStatus.STOPPING: 'Terminating',
    EnvironmentStatus.STOPPED: 'Inactive',
    EnvironmentStatus.FAILED: 'Aborted',
}

class EnvironmentWaiter:
    def __init__(self, client: TorqueClient, space: str, environment_id: str):
        self.client = client
        self.space = space
        self.environment_id = environment_id

    def wait_for_status(self, desired: EnvironmentStatus, timeout: int = 600, interval: int = DEFAULT_POLL_INTERVAL) -> EnvironmentResponse:
        target_phase = PHASE_MAP.get(desired, desired.value)
        start = time.time()
        while True:
            env = self.client.get_spaces_by_space_name_environments_by_environment_id(self.space, self.environment_id)
            phase_obj = env.details.state.current_state if (env.details and env.details.state and env.details.state.current_state is not None) else None
            # current_state may be represented as dict like {'Active': None} or a simple string
            matches = False
            if isinstance(phase_obj, dict):
                matches = target_phase in phase_obj
            elif isinstance(phase_obj, str):
                matches = phase_obj == target_phase
            if matches:
                return env
            if time.time() - start > timeout:
                raise TimeoutError(f"Timed out waiting for status {desired}")
            time.sleep(interval)

from pytorque.utils import EnvironmentWaiter
from pytorque.models.environment import EnvironmentStatus
from pydantic import BaseModel

class _StubDetails(BaseModel):
    id: str

class _StubEnv(BaseModel):
    details: _StubDetails

def test_waiter_reaches_status(monkeypatch):
    dummy_env = _StubEnv(details=_StubDetails(id='e1'))
    monkeypatch.setattr(EnvironmentWaiter, 'wait_for_status', lambda self, desired, timeout=0, interval=0: dummy_env)
    waiter = EnvironmentWaiter(client=None, space='space1', environment_id='e1')  # type: ignore[arg-type]
    env = waiter.wait_for_status(EnvironmentStatus.RUNNING)
    assert env.details.id == 'e1'

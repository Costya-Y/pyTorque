from pytorque.utils import EnvironmentWaiter
from pytorque.models.environment import Environment, EnvironmentStatus
from pytorque.client import TorqueClient
from pytorque.config import TorqueConfig
import time
import pytest

class DummyResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self._json = json_data
        self.text = str(json_data)
    def json(self):
        return self._json

class DummyHTTPClient:
    def __init__(self, env_sequence):
        self.env_sequence = env_sequence
        self.calls = 0
    def get(self, path):
        if path.startswith('/environments/'):
            idx = min(self.calls, len(self.env_sequence)-1)
            env = self.env_sequence[idx]
            self.calls += 1
            return DummyResponse(200, env)
        return DummyResponse(404, {})

@pytest.fixture
def client(monkeypatch):
    cfg = TorqueConfig(base_url='https://example/api', api_token='x')
    c = TorqueClient(cfg)
    seq = [
        {'id':'e1','name':'Env1','status':'PENDING'},
        {'id':'e1','name':'Env1','status':'STARTING'},
        {'id':'e1','name':'Env1','status':'RUNNING'},
    ]
    dummy = DummyHTTPClient(seq)
    # Inject dummy HTTP client by setting protected attribute used by property
    monkeypatch.setattr(c, '_client', dummy, raising=False)
    return c

def test_waiter_reaches_status(client, monkeypatch):
    waiter = EnvironmentWaiter(client, 'e1')
    monkeypatch.setattr(time, 'sleep', lambda s: None)
    env = waiter.wait_for_status(EnvironmentStatus.RUNNING, timeout=30, interval=0)
    assert env.status == EnvironmentStatus.RUNNING

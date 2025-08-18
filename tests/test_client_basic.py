import pytest
from pytorque.client import TorqueClient
from pytorque.config import TorqueConfig

class DummyResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self._json = json_data
        self.text = str(json_data)
    def json(self):
        return self._json

class DummyHTTPClient:
    def __init__(self, responses):
        self.responses = responses
    def get(self, path):
        return self.responses.get(('GET', path))
    def post(self, path, json=None):
        return self.responses.get(('POST', path))

@pytest.fixture
def client(monkeypatch):
    cfg = TorqueConfig(base_url='https://example/api', api_token='x')
    c = TorqueClient(cfg)
    dummy = DummyHTTPClient({
        ('GET', '/blueprints'): DummyResponse(200, [{'id':'b1','name':'BP1'}]),
        ('GET', '/environments'): DummyResponse(200, [{'id':'e1','name':'Env1','status':'RUNNING'}]),
        ('GET', '/environments/e1'): DummyResponse(200, {'id':'e1','name':'Env1','status':'RUNNING'}),
        ('POST', '/environments'): DummyResponse(200, {'id':'e2','name':'Env2','status':'PENDING'}),
        ('POST', '/environments/e1/stop'): DummyResponse(200, {'result':'stopping'}),
    })
    # Inject dummy HTTP client by setting protected attribute used by property
    monkeypatch.setattr(c, '_client', dummy, raising=False)
    return c

def test_list_blueprints(client):
    bps = client.list_blueprints()
    assert bps[0].id == 'b1'

def test_list_environments(client):
    envs = client.list_environments()
    assert envs[0].id == 'e1'

def test_get_environment(client):
    env = client.get_environment('e1')
    assert env.name == 'Env1'

def test_launch_environment(client):
    env = client.launch_environment('b1', name='Env2')
    assert env.id == 'e2'

def test_stop_environment(client):
    r = client.stop_environment('e1')
    assert r['result'] == 'stopping'

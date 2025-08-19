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
    def request(self, method, path, params=None, json=None, **kwargs):
        return self.responses.get((method, path))

@pytest.fixture
def client(monkeypatch):
    cfg = TorqueConfig(base_url='https://example/api', api_token='x')
    c = TorqueClient(cfg)
    dummy = DummyHTTPClient({
        ('GET', '/spaces/space1/blueprints'): DummyResponse(200, [{'blueprint_name':'b1','name':'BP1'}]),
        ('GET', '/spaces/space1/environments/v2'): DummyResponse(200, {'environment_list':[{'id':'e1'}]}),
        ('GET', '/spaces/space1/environments/e1'): DummyResponse(200, { 'details': { 'id':'e1', 'state': { 'current_state': {'Active': None } } } }),
        ('POST', '/spaces/space1/environments'): DummyResponse(200, {'id':'e2'}),
        ('DELETE', '/spaces/space1/environments/e1'): DummyResponse(200, {'result':'stopping'}),
    })
    # Inject dummy HTTP client by setting protected attribute used by property
    monkeypatch.setattr(c, '_client', dummy, raising=False)
    return c

def test_list_blueprints(client):
    bps = client.get_spaces_by_space_name_blueprints('space1')
    assert bps[0].blueprint_name == 'b1'

def test_list_environments(client):
    envs_resp = client.get_spaces_by_space_name_environments_v2('space1')
    assert envs_resp.environment_list[0].id == 'e1'

def test_get_environment(client):
    env = client.get_spaces_by_space_name_environments_by_environment_id('space1','e1')
    assert env.details.id == 'e1'

def test_launch_environment(client):
    env = client.post_spaces_by_space_name_environments('space1', body=None)
    assert env.id == 'e2'

def test_stop_environment(client):
    r = client.delete_spaces_by_space_name_environments_by_environment_id('space1','e1')
    assert r['result'] == 'stopping'

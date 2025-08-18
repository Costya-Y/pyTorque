from pytorque.config import TorqueConfig, TOKEN_ENV_VAR, BASE_URL_ENV_VAR, DEFAULT_BASE_URL
import os

def test_config_from_env(monkeypatch):
    monkeypatch.setenv(TOKEN_ENV_VAR, 'abc123')
    monkeypatch.setenv(BASE_URL_ENV_VAR, 'https://example.com/api')
    cfg = TorqueConfig.from_env()
    assert cfg.api_token == 'abc123'
    assert cfg.base_url == 'https://example.com/api'

def test_headers():
    cfg = TorqueConfig(base_url=DEFAULT_BASE_URL, api_token='tkn')
    h = cfg.headers()
    assert h['Authorization'] == 'Bearer tkn'
    assert 'User-Agent' in h

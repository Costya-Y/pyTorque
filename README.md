# pyTorque

Python client library for the Quali Torque SaaS API.

## Features (initial roadmap)
- Auth (API token / OAuth PAT) support via environment variable `TORQUE_API_TOKEN`.
- Async + sync clients built on `httpx`.
- Environment (blueprint) listing, launch, status, stop.
- Activity / job tracking with polling helper.
- Typed models via Pydantic v2.

## Installation
```bash
pip install pytorque
```
(For local dev)
```bash
pip install -e .[dev]
```

## Quick Start
```python
from pytorque import TorqueClient

client = TorqueClient(base_url="https://portal.qtorque.io", api_token="<TOKEN>")
or
client = TorqueClient() assuming requested environment variable properly set.

blueprints = client.get_spaces_by_space_name_catalog(space_name="NAMESPACE")
print(blueprints)
```

## Environment Variables
- `TORQUE_API_TOKEN` – default token if not passed explicitly.
- `TORQUE_BASE_URL` – (optional) default base URL (e.g. `https://portal.qtorque.io`).

## Development
Run tests:
```bash
pytest
```

## License
Apache 2.0

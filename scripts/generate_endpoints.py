#!/usr/bin/env python
"""Generate endpoint method stubs from OpenAPI document.

This script reads document.yaml and updates src/pytorque/endpoints.py with
simple wrapper methods. It intentionally keeps models as generic Dict[str, Any]
until specialized pydantic models are added.
"""
from __future__ import annotations
import re
import yaml
from pathlib import Path
from textwrap import indent

ROOT = Path(__file__).resolve().parents[1]
OPENAPI_FILE = ROOT / "document.yaml"
OUT_FILE = ROOT / "src" / "pytorque" / "endpoints.py"

HTTP_METHODS = {"get", "post", "put", "delete", "patch", "options", "head"}

def snake(name: str) -> str:
    name = name.strip().lower()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    name = re.sub(r"_+", "_", name)
    return name.strip("_")

def path_to_method_base(path: str) -> str:
    # remove /api/ prefix
    p = path.lstrip('/')
    if p.startswith('api/'):
        p = p[4:]
    segments = []
    for seg in p.split('/'):
        if seg.startswith('{') and seg.endswith('}'):
            key = seg[1:-1]
            segments.append('by_' + snake(key))
        else:
            segments.append(snake(seg))
    return '_'.join(segments)

def build_param_list(path_params, query_params):
    params = []
    for p in path_params:
        params.append(f"{p}: str")
    if query_params:
        params.append("query: dict | None = None")
    params.append("**kwargs")  # forward any additional args (json, data, headers)
    return ", ".join(params)

def build_url_expr(path: str) -> str:
    # convert /api/spaces/{space_name}/blueprints -> f"/spaces/{space_name}/blueprints"
    inner = path
    if inner.startswith('/api'):
        inner = inner[4:]
    return 'f"' + inner.replace('{', '{') + '"'

def main():
    spec = yaml.safe_load(OPENAPI_FILE.read_text())
    paths = spec.get('paths', {})
    lines = [
        "from __future__ import annotations",
        "from typing import Any, Dict, List, Optional",
        "import httpx",
        "from .client import TorqueClient, AsyncTorqueClient",
        "",
        "# AUTO-GENERATED: Do not edit manually. Run scripts/generate_endpoints.py",
        "",
    ]
    sync_methods = []
    async_methods = []
    for path, path_item in paths.items():
        for method, op in path_item.items():
            if method not in HTTP_METHODS:
                continue
            summary = op.get('summary') or ''
            params = op.get('parameters', [])
            path_params = [p['name'] for p in params if p.get('in') == 'path']
            query_params = [p['name'] for p in params if p.get('in') == 'query']
            base_name = path_to_method_base(path)
            method_name = f"{method}_{base_name}"[:100]
            param_list = build_param_list(path_params, query_params)
            url_expr = build_url_expr(path)
            doc = summary.replace('"', '\"')
            query_build = "query" if query_params else "None"
            sync_body = f"def {method_name}(self, {param_list}):\n    \"\"\"{doc}\n    Auto-generated from OpenAPI.\n    \"\"\"\n    url = {url_expr}\n    return self._handle_response(self.client.request(\"{method.upper()}\", url, params={query_build}, **kwargs))\n"
            async_body = f"async def {method_name}(self, {param_list}):\n    \"\"\"{doc}\n    Auto-generated from OpenAPI.\n    \"\"\"\n    url = {url_expr}\n    resp = await self.client.request(\"{method.upper()}\", url, params={query_build}, **kwargs)\n    return self._handle_response(resp)\n"
            sync_methods.append(sync_body)
            async_methods.append(async_body)
    lines.append("class TorqueEndpointsMixin:")
    lines.extend(indent(m, '    ') for m in sync_methods or ["pass\n"])
    lines.append("")
    lines.append("class AsyncTorqueEndpointsMixin:")
    lines.extend(indent(m, '    ') for m in async_methods or ["pass\n"])
    OUT_FILE.write_text("\n".join(lines))
    print(f"Generated {len(sync_methods)} sync and {len(async_methods)} async endpoint methods -> {OUT_FILE}")

if __name__ == "__main__":
    main()

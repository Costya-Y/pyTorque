#!/usr/bin/env python
"""Generate endpoint method stubs from OpenAPI document with model binding.

Enhancements:
    * Detect JSON response schema and map $ref'd components to generated Pydantic models.
    * For array responses referencing a component, return List[Model].
    * Accept request body (application/json) as either a Pydantic model instance or a plain dict via a 'body' param.
    * Provide type annotations for return values.
"""
from __future__ import annotations
import re
import yaml
from pathlib import Path
from textwrap import indent
from typing import Any, Dict

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

def build_param_list(path_params, query_params, has_body: bool):
    params = []
    for p in path_params:
        params.append(f"{p}: str")
    if query_params:
        params.append("query: dict | None = None")
    if has_body:
        params.append("body: Any | None = None")
    params.append("**kwargs")  # forward additional args
    return ", ".join(params)

def build_url_expr(path: str) -> str:
    # convert /api/spaces/{space_name}/blueprints -> f"/spaces/{space_name}/blueprints"
    inner = path
    if inner.startswith('/api'):
        inner = inner[4:]
    return 'f"' + inner.replace('{', '{') + '"'

def _response_model_info(op: Dict[str, Any]) -> tuple[str | None, bool]:
    """Return (model_name, is_array)."""
    responses = op.get("responses", {}) or {}
    # pick first success code
    success_codes = sorted([c for c in responses.keys() if c.isdigit() and c.startswith("2")])
    for code in success_codes:
        content = responses.get(code, {}).get("content", {}) or {}
        schema = content.get("application/json", {}).get("schema") if content else None
        if not schema:
            continue
        # array
        if schema.get("type") == "array":
            items = schema.get("items", {})
            if "$ref" in items:
                ref = items["$ref"].split("/")[-1]
                return ref, True
        if "$ref" in schema:
            ref = schema["$ref"].split("/")[-1]
            return ref, False
    return None, False

def _request_body_model(op: Dict[str, Any]) -> str | None:
    rb = op.get("requestBody") or {}
    content = rb.get("content", {})
    schema = content.get("application/json", {}).get("schema") if content else None
    if not schema:
        return None
    if "$ref" in schema:
        return schema["$ref"].split("/")[-1]
    if schema.get("type") == "array" and "$ref" in schema.get("items", {}):
        return schema["items"]["$ref"].split("/")[-1]
    # allOf single ref
    if "allOf" in schema:
        for part in schema["allOf"]:
            if "$ref" in part:
                return part["$ref"].split("/")[-1]
    return None

def main():
    spec = yaml.safe_load(OPENAPI_FILE.read_text())
    paths = spec.get('paths', {})
    used_models: set[str] = set()
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
            resp_model, is_array = _response_model_info(op)
            req_model = _request_body_model(op)
            if resp_model:
                used_models.add(resp_model)
            if req_model:
                used_models.add(req_model)
            base_name = path_to_method_base(path)
            method_name = f"{method}_{base_name}"[:120]
            param_list = build_param_list(path_params, query_params, bool(req_model))
            url_expr = build_url_expr(path)
            doc = summary.replace('"', '\"')
            query_build = "query" if query_params else "None"
            # build request body fragment
            if req_model:
                body_json = "(body.model_dump(by_alias=True, exclude_none=True) if hasattr(body, 'model_dump') else body) if body is not None else None"
                body_arg = f", json={body_json}"
            else:
                body_arg = ""
            # return annotation
            if resp_model:
                model_class = resp_model.split('.')[-1]
                if is_array:
                    ret_ann = f"List[{model_class}]"
                    parse_code = f"data = self._handle_response(resp); return [ {model_class}.model_validate(d) for d in data ]"
                else:
                    ret_ann = model_class
                    parse_code = f"data = self._handle_response(resp); return {model_class}.model_validate(data)"
            else:
                ret_ann = "Any"
                parse_code = "return self._handle_response(resp)"
            sync_body = (
                f"def {method_name}(self, {param_list}) -> {ret_ann}:\n"
                f"    \"\"\"{doc}\n    Auto-generated from OpenAPI.\n    \"\"\"\n"
                f"    url = {url_expr}\n"
                f"    resp = self.torque_client.request(\"{method.upper()}\", url, params={query_build}{body_arg}, **kwargs)\n"
                f"    {parse_code}\n"
            )
            async_body = (
                f"async def {method_name}(self, {param_list}) -> {ret_ann}:\n"
                f"    \"\"\"{doc}\n    Auto-generated from OpenAPI.\n    \"\"\"\n"
                f"    url = {url_expr}\n"
                f"    resp = await self.torque_client.request(\"{method.upper()}\", url, params={query_build}{body_arg}, **kwargs)\n"
                f"    {parse_code}\n"
            )
            sync_methods.append(sync_body)
            async_methods.append(async_body)

    # Build header/import lines
    lines = [
        "from __future__ import annotations",
        "from typing import Any, Dict, List, Optional",
        "import httpx  # noqa: F401",
        "from pydantic import BaseModel  # noqa: F401",
        "from .models.generated import *  # noqa: F401,F403",  # export models
        "",
        "# AUTO-GENERATED: Do not edit manually. Run scripts/generate_endpoints.py",
        "",
        "from typing import Protocol, runtime_checkable",
        "@runtime_checkable\nclass _SupportsRequest(Protocol):\n    def _handle_response(self, resp: Any) -> Any: ...\n    @property\n    def torque_client(self): ...",
        "",
        "class TorqueEndpointsMixin(_SupportsRequest):",
    ]
    lines.extend(indent(m, '    ') for m in sync_methods or ["pass\n"])
    lines.append("")
    lines.append("class AsyncTorqueEndpointsMixin(_SupportsRequest):")
    lines.extend(indent(m, '    ') for m in async_methods or ["pass\n"])
    OUT_FILE.write_text("\n".join(lines))
    print(f"Generated {len(sync_methods)} sync and {len(async_methods)} async endpoint methods -> {OUT_FILE}")

if __name__ == "__main__":
    main()

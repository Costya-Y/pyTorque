#!/usr/bin/env python
"""Generate Pydantic models from OpenAPI components.schemas.

Usage:
    python scripts/generate_models.py [spec_path=document.yaml] [out_path=src/pytorque/models/generated.py]

Notes:
    - Pragmatic generator (not full JSON Schema implementation).
    - Supports: properties, required, nullable, $ref, arrays, additionalProperties, allOf (simple merge).
    - Produces Pydantic BaseModel subclasses.
    - Name mapping: last dotted segment of schema key; collisions resolved by suffix.
"""
from __future__ import annotations

import re
import sys
import keyword
from pathlib import Path
from typing import Any, Dict, List, Set

import yaml

PRIMITIVE_TYPE_MAP = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
}


def sanitize_name(name: str) -> str:
    base = name.split(".")[-1]
    base = re.sub(r"[^0-9a-zA-Z_]", "_", base)
    if not re.match(r"[A-Za-z_]", base):
        base = f"_{base}"
    if keyword.iskeyword(base):
        base += "_"
    return base


def collect_schemas(spec: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    return spec.get("components", {}).get("schemas", {})


def resolve_allof(schema: Dict[str, Any], schemas: Dict[str, Any]) -> Dict[str, Any]:
    if "allOf" not in schema:
        return schema
    merged: Dict[str, Any] = {k: v for k, v in schema.items() if k != "allOf"}
    properties: Dict[str, Any] = {}
    required: Set[str] = set()
    for part in schema["allOf"]:
        if "$ref" in part:
            ref_name = part["$ref"].split("/")[-1]
            ref_schema = resolve_allof(schemas.get(ref_name, {}), schemas)
            properties.update(ref_schema.get("properties", {}))
            required.update(ref_schema.get("required", []))
        else:
            properties.update(part.get("properties", {}))
            required.update(part.get("required", []))
    properties.update(schema.get("properties", {}))
    required.update(schema.get("required", []))
    merged["properties"] = properties
    if required:
        merged["required"] = sorted(required)
    return merged


def ref_to_class(ref: str, name_map: Dict[str, str]) -> str:
    target = ref.split("/")[-1]
    return name_map.get(target, sanitize_name(target))


def property_type(prop: Dict[str, Any], name_map: Dict[str, str]) -> str:
    if "$ref" in prop:
        return ref_to_class(prop["$ref"], name_map)
    if "allOf" in prop and len(prop["allOf"]) == 1 and "$ref" in prop["allOf"][0]:
        return ref_to_class(prop["allOf"][0]["$ref"], name_map)
    t = prop.get("type")
    if t == "array":
        items = prop.get("items", {})
        inner = property_type(items, name_map) if items else "Any"
        return f"List[{inner}]"
    if t == "object":
        addl = prop.get("additionalProperties")
        if isinstance(addl, dict):
            inner = property_type(addl, name_map)
            return f"Dict[str, {inner}]"
        return "Dict[str, Any]"
    return PRIMITIVE_TYPE_MAP.get(t, "Any")


def generate_model_code(spec: Dict[str, Any]) -> str:
    schemas = collect_schemas(spec)
    name_map: Dict[str, str] = {}
    used: Set[str] = set()
    for raw in schemas.keys():
        candidate = sanitize_name(raw)
        base = candidate
        i = 1
        while candidate in used:
            candidate = f"{base}{i}"
            i += 1
        name_map[raw] = candidate
        used.add(candidate)

    lines: List[str] = []
    lines.append("# AUTO-GENERATED: Do not edit manually. Run scripts/generate_models.py")
    lines.append("from __future__ import annotations")
    lines.append("from typing import Any, Dict, List, Optional")
    lines.append("from pydantic import BaseModel, Field")
    lines.append("")
    lines.append("__all__ = []  # populated at end")
    lines.append("")
    lines.append("SCHEMA_NAME_MAP = {")
    for raw, cls in sorted(name_map.items()):
        lines.append(f"    \"{raw}\": \"{cls}\",")
    lines.append("}")
    lines.append("")

    for raw_name, schema in schemas.items():
        schema = resolve_allof(schema, schemas)
        cls_name = name_map[raw_name]
        desc = schema.get("description", "")
        props: Dict[str, Any] = schema.get("properties", {}) or {}
        required = set(schema.get("required", []))
        lines.append(f"class {cls_name}(BaseModel):")
        if not props:
            if desc:
                lines.append(f"    \"\"\"{desc}\"\"\"")
            lines.append("    pass")
            lines.append("")
            continue
        if desc:
            lines.append(f"    \"\"\"{desc}\"\"\"")
        for original_pname, pinfo in props.items():
            pname = original_pname
            safe_pname = re.sub(r'[^0-9a-zA-Z_]', '_', pname)
            pname_alias: str | None = None
            if safe_pname != pname:
                pname_alias = pname
                pname = safe_pname
            annotation = property_type(pinfo, name_map)
            nullable = pinfo.get("nullable", False)
            is_required = pname in required and not nullable
            if (not is_required) or nullable:
                annotation = f"Optional[{annotation}]"
            field_args = []
            pdesc = pinfo.get("description")
            if pdesc:
                safe_desc = " ".join(pdesc.split())  # collapse newlines/extra spaces
                safe_desc = safe_desc.replace("\\", " ").replace('"', '\\"')
                field_args.append(f"description=\"{safe_desc}\"")
            if pname_alias:
                field_args.append(f"alias=\"{pname_alias}\"")
            default_expr = "..." if is_required else "None"
            if field_args:
                lines.append(f"    {pname}: {annotation} = Field({default_expr}, {', '.join(field_args)})")
            else:
                lines.append(f"    {pname}: {annotation} = {default_expr}")
        lines.append("")
        lines.append(f"__all__.append(\"{cls_name}\")")
        lines.append("")

    return "\n".join(lines)


def main():
    spec_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("document.yaml")
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("src/pytorque/models/generated.py")
    spec = yaml.safe_load(spec_path.read_text(encoding="utf-8"))
    code = generate_model_code(spec)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(code, encoding="utf-8")
    print(f"Generated models: {out_path} ({out_path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

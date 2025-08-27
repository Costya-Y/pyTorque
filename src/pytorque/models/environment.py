from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
import yaml
import json
from yaml.error import YAMLError

class EnvironmentStatus(str, Enum):
    PENDING = "PENDING"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    FAILED = "FAILED"

class Environment(BaseModel):
    id: str = Field(..., description="Environment ID")
    name: str
    blueprint_id: Optional[str] = None
    status: EnvironmentStatus
    created_by: Optional[str] = None
    created_at: Optional[str] = None  # ISO datetime
    updated_at: Optional[str] = None
    outputs: Optional[Dict[str, Any]] = None
    links: Optional[List[Dict[str, Any]]] = None

class Blueprint(BaseModel):
    id: str
    name: str
    description: Optional[str] = None

class GrainSpec(BaseModel):
    commands: List[Any] = Field(default_factory=list)
    env_vars: List[Any] = Field(default_factory=list, alias="env-vars")
    inputs: List[Any] = Field(default_factory=list)
    outputs: List[Any] = Field(default_factory=list)
    source: Dict[str, Any] = Field(default_factory=dict)

class Grain(BaseModel):
    name: str
    depends_on: Optional[str] = Field(None, alias="depends-on")
    kind: Optional[str] = None
    spec: GrainSpec

    def update_grain_input(self, new_inputs: Dict[str, Any]) -> None:
        for input in new_inputs:
            env_input = next(x for x in self.spec.inputs if x.get(input))
            self.spec.inputs.remove(env_input)
            self.spec.inputs.append({input: new_inputs[input]})

class EnvironmentMeta(BaseModel):
    environment_name: Optional[str] = None
    owner_email: Optional[str] = None
    state: Optional[str] = None

class EnvironmentEacSpec(BaseModel):
    """Structured representation of an environment EAC YAML export.

    Fields:
        meta: high-level environment metadata (environment: section)
        grains: mapping of grain name -> Grain
        inputs: top-level inputs mapping
        outputs: top-level outputs mapping
        spec_version: version integer
        raw: original raw dict for forward compatibility
    """
    meta: EnvironmentMeta
    grains: Dict[str, Grain]
    inputs: Dict[str, Any] = Field(default_factory=dict)
    outputs: Dict[str, Any] = Field(default_factory=dict)
    spec_version: Optional[int] = Field(None, alias="spec_version")
    raw: Dict[str, Any]

    @classmethod
    def from_yaml(cls, text: str) -> "EnvironmentEacSpec":
        """Parse an Environment EAC export YAML string.

        The Torque service sometimes returns YAML that includes trailing commas
        after mapping values (a JSON style that standard YAML forbids). To be
        resilient we attempt standard safe_load first, then (on failure) apply a
        light normalization pass that removes trailing commas from scalar lines
        and retries. As an additional fallback, if the content looks like JSON
        we attempt json.loads.
        """

        def _try_yaml(data: str) -> Dict[str, Any]:
            loaded = yaml.safe_load(data) or {}
            if not isinstance(loaded, dict):
                raise ValueError("EAC YAML root must be a mapping")
            return loaded

        # Remove uniform leading indentation (common in triple-quoted tests)
        lines = text.splitlines()
        non_empty = [l for l in lines if l.strip()]
        if non_empty:
            # Compute minimal leading spaces across non-empty lines
            import re
            leading = min(len(re.match(r'^[ \t]*', l).group(0)) for l in non_empty)  # type: ignore[arg-type]
            if leading:
                text = '\n'.join(l[leading:] if len(l) >= leading else l for l in lines)
        try:
            raw = _try_yaml(text)
        except YAMLError:
            # Relaxed mode: strip trailing commas at end-of-line for simple key/value lines.
            normalized_lines: List[str] = []
            for line in text.splitlines():
                stripped = line.rstrip()
                # If line looks like key: value, and ends with a trailing comma, drop the comma (even for [], {}).
                if ':' in stripped and stripped.endswith(','):
                    stripped = stripped[:-1]
                normalized_lines.append(stripped)
            normalized_text = '\n'.join(normalized_lines)
            try:
                raw = _try_yaml(normalized_text)
            except YAMLError:
                # Last resort: try JSON (after removing trailing commas that would invalidate JSON)
                json_candidate = normalized_text
                try:
                    raw_json = json.loads(json_candidate)
                    if isinstance(raw_json, dict):
                        raw = raw_json
                    else:
                        raise ValueError("EAC export is not a mapping after JSON parse attempt")
                except Exception as e:  # noqa: BLE001 - want original context
                    raise ValueError("Failed to parse EAC YAML/JSON export") from e
        env_meta = EnvironmentMeta(**(raw.get("environment", {}) or {}))
        grains_raw = raw.get("grains", {}) or {}
        grains: Dict[str, Grain] = {}
        for gname, gdata in grains_raw.items():
            if not isinstance(gdata, dict):
                continue
            spec_data = gdata.get("spec", {}) or {}
            payload = {
                "name": gname,
                "depends-on": gdata.get("depends-on"),
                "kind": gdata.get("kind"),
                "spec": spec_data,
            }
            grain = Grain(**payload)
            grains[gname] = grain
        return cls(
            meta=env_meta,
            grains=grains,
            inputs=raw.get("inputs", {}) or {},
            outputs=raw.get("outputs", {}) or {},
            spec_version=raw.get("spec_version"),
            raw=raw,
        )

    def grain_names(self) -> List[str]:  # convenience helper
        return list(self.grains.keys())

    def get_grain(self, name: str) -> Optional[Grain]:
        return self.grains.get(name)

    # ------------------------------------------------------------------
    # Serialization helpers
    # ------------------------------------------------------------------
    def to_dict(self) -> Dict[str, Any]:
        """Return a dictionary representation mirroring the original EAC export layout.

        The ordering of keys is preserved (Python 3.7+ dicts keep insertion order),
        so subsequent ``yaml.safe_dump(sort_keys=False)`` calls will keep the same
        relative ordering for readability and diff-friendliness.
        """
        grains_dict: Dict[str, Any] = {}
        for gname, grain in self.grains.items():
            grain_payload: Dict[str, Any] = {}
            if grain.depends_on is not None:
                grain_payload["depends-on"] = grain.depends_on
            if grain.kind is not None:
                grain_payload["kind"] = grain.kind
            # Use by_alias to emit 'env-vars'
            grain_payload["spec"] = grain.spec.model_dump(by_alias=True, exclude_none=True)
            grains_dict[gname] = grain_payload

        root: Dict[str, Any] = {}
        # environment metadata
        env_meta = self.meta.model_dump(exclude_none=True)
        if env_meta:
            root["environment"] = env_meta
        # grains
        root["grains"] = grains_dict
        # always include inputs/outputs even if empty to be explicit
        root["inputs"] = self.inputs or {}
        root["outputs"] = self.outputs or {}
        if self.spec_version is not None:
            root["spec_version"] = self.spec_version
        return root

    def to_yaml(self) -> str:
        """Serialize the spec back to a YAML string.

        Uses ``yaml.safe_dump`` with ``sort_keys=False`` to preserve insertion
        order (matching original parse order), minimizing noisy diffs.
        """
        data = self.to_dict()
        return yaml.safe_dump(data, sort_keys=False)

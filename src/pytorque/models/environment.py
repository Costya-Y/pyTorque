from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
import yaml

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
        raw = yaml.safe_load(text) or {}
        if not isinstance(raw, dict):
            raise ValueError("EAC YAML root must be a mapping")
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

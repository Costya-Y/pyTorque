from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List

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

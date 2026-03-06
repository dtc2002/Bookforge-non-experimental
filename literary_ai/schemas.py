from pydantic import BaseModel
from typing import List, Dict, Optional

class ProjectConfig(BaseModel):
    name: str
    author: str
    settings: Dict[str, Any]

class UniverseBible(BaseModel):
    entities: Dict[str, Dict]
    story_artifacts: List[Dict]

class Character(BaseModel):
    id: str
    name: str
    role: str
    traits: Dict[str, Any]

class PlotThread(BaseModel):
    id: str
    title: str
    summary: str
    key_events: List[str]

class CanonFact(BaseModel):
    id: str
    statement: str
    sources: List[str]

class CheckerFinding(BaseModel):
    id: str
    severity: str
    description: str
    suggestions: List[str]
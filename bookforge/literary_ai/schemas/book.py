from .base import BaseArtifact
from pydantic import field_validator
from datetime import datetime


class Book(BaseArtifact):
    title: str
    author: str
    chapters: list[str]

    @field_validator("created_at", "updated_at")
    def validate_datetime(cls, v):
        if not isinstance(v, str):
            return datetime.now().isoformat()
        return v
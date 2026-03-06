from pydantic import BaseModel
from typing import Dict, Any

class BaseArtifact(BaseModel):
    id: str
    type: str
    created_at: str
    updated_at: str

    def to_dict(self) -> Dict[str, Any]:
        return self.dict()
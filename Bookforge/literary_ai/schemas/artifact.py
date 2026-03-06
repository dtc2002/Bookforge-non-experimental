from pydantic import BaseModel

class ArtifactSchema(BaseModel):
    id: str
    content: str
    metadata: dict
    created_at: str
    updated_at: str

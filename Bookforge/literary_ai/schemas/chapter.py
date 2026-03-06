from pydantic import BaseModel

class ChapterSchema(ArtifactSchema):
    chapter_number: int
    title: str
    section: str
    content: str

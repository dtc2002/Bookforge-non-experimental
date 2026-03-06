from pydantic import BaseModel

class BookSchema(ArtifactSchema):
    title: str
    author: str
    chapters: list[ChapterSchema]
    cover_art: str
    publication_date: str

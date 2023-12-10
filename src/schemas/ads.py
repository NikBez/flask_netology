from datetime import datetime

from pydantic import BaseModel


class AdBaseSchema(BaseModel):
    title: str
    description: str
    created_at: datetime
    author: str


class ADCreateSchema(AdBaseSchema):
    pass


class AdUpdateSchema(AdBaseSchema):
    title: str | None = None
    description: str | None = None
    created_at: datetime | None = None
    author: str | None = None


class ADSchema(AdBaseSchema):
    id: int

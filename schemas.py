from pydantic import BaseModel


class ArticleSchemaIn(BaseModel):
    title: str
    description: str


class ArticleSchema(BaseModel):
    id: int
    title: str
    description: str

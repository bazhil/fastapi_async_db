from pydantic import BaseModel


class ArticleSchemaIn(BaseModel):
    title: str
    description: str


class ArticleSchema(BaseModel):
    id: int
    title: str
    description: str

class UserSchemaIn(BaseModel):
    username: str
    password: str

class UserSchema(BaseModel):
    id: int
    username: str

from fastapi import APIRouter, status, HTTPException
from schemas import ArticleSchemaIn, ArticleSchema
from typing import List
from db import database, Article

router = APIRouter()


@router.post('/users', status_code=status.HTTP_201_CREATED)
async def insert_user(article: UserSchemaIn):

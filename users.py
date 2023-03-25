from fastapi import APIRouter, status, HTTPException
from schemas import UserSchemaIn
from typing import List
from db import database, User

router = APIRouter()


@router.post('/users', status_code=status.HTTP_201_CREATED)
async def insert_user(user: UserSchemaIn):
    query = User.insert(username=user.username, password=user.password)
    last_record_id = await database.execute(query)
    return {**user.dict(), 'id': last_record_id}

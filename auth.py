from datetime import timedelta

from fastapi import APIRouter, status, HTTPException
from schemas import LoginSchema
from typing import List
from db import database, Article, User
from passlib.hash import pbkdf2_sha256

from Token import create_access_token

router = APIRouter(
    tags = ['Auth']
)

@router.post('/login/')
async def login(request: LoginSchema):
    query = User.select().where(User.c.username == request.username)
    myuser = await database.fetch_one(query=query)

    if not myuser:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details='User does not found')

    if not pbkdf2_sha256.verify(request.password, myuser.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details='Invalid password')

    access_token = create_access_token(data={"sub": myuser.username})
    return {"access_token": access_token, "token_type": "bearer"}

from fastapi import APIRouter, status, HTTPException
from schemas import LoginSchema
from typing import List
from db import database, Article, User
from passlib.hash import pbkdf2_sha256


router = APIRouter(
    tags = ['Auth']
)

@router.post('/login/')
async def login(request: LoginSchema):
    query = User.select().where(User.c.username == request.username)
    myuser = await database.fetch_one(query=query)

    if not myuser:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details='User does not found')

    if not pbkdf2_sha256.veriofy(request.password, myuser.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details='Invalid password')

    return myuser

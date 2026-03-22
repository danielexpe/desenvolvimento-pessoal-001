from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

# Simulated database for example purposes
users_db = {}
tokens_db = {}

class User(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'

@router.post('/auth/register', response_model=UserResponse)
async def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail='User already registered')
    users_db[user.username] = user.password  # Simulating saving to a database
    return UserResponse(username=user.username)

@router.post('/auth/login', response_model=Token)
async def login(user: User):
    if user.username not in users_db or users_db[user.username] != user.password:
        raise HTTPException(status_code=401, detail='Invalid credentials')
    # Simulate JWT creation
    access_token = f'token_for_{user.username}'
    tokens_db[user.username] = access_token  # Simulating saving token
    return Token(access_token=access_token)

@router.get('/auth/me', response_model=UserResponse)
async def get_current_user(username: str):
    if username not in users_db:
        raise HTTPException(status_code=404, detail='User not found')
    return UserResponse(username=username)

@router.post('/auth/refresh', response_model=Token)
async def refresh_token(username: str):
    if username not in tokens_db:
        raise HTTPException(status_code=404, detail='Token not found')
    # Simulate generating a new token
    new_access_token = f'new_token_for_{username}'
    tokens_db[username] = new_access_token  # Simulating saving new token
    return Token(access_token=new_access_token)
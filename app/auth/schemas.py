import uuid

from pydantic import EmailStr
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    login: str
    role: str

class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    login: str 
    role: str 


class UserUpdate(schemas.BaseUserUpdate):
    pass
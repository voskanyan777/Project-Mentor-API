from enum import Enum
from pydantic import EmailStr
from fastapi_users import schemas


class RoleEnum(str, Enum):
    user = 'User'
    mentor = 'Mentor'

class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    role: str

class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    role: RoleEnum 


class UserUpdate(schemas.BaseUserUpdate):
    pass
from pydantic import BaseModel


class UserCreate(BaseModel):
    login: str
    name: str
    surname: str
    email: str
    password: str
    role: str = 'user'

class UserLogin(BaseModel):
    email: str
    password: str
from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    user_login: str
    user_name: str
    user_surname: str
    user_email: str
    password: str
    user_role: str = 'user'
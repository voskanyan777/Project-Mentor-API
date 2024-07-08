from pydantic import BaseModel


class UserCreate(BaseModel):
    user_login: str
    user_name: str
    user_surname: str
    user_email: str
    password: str
    user_role: str = 'user'

class UserLogin(BaseModel):
    user_email: str
    user_password: str
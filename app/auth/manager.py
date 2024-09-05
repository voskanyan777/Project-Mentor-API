import os
from typing import Optional

from db.database import get_user_db
from db.models import User
from dotenv import load_dotenv
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from .tasks import send_message, send_verify_email

load_dotenv()

SECRET = os.getenv('SECRET_AUTH_KEY')


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        send_message.delay(user.email)

    async def on_after_forgot_password(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        print(token)
    
    async def on_after_request_verify(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        print(token)
        send_verify_email.delay(user.email, token)

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

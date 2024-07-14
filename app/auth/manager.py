import os
import smtplib
from dotenv import load_dotenv
from typing import Optional

from email.message import EmailMessage
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from db.models import User
from db.database import get_user_db


load_dotenv()

SECRET = os.getenv('SECRET_AUTH_KEY')

login = os.getenv("EMAIL_LOGIN")
password = os.getenv('EMAIL_PASSWORD') 

def send_message(user_email: str):
    email = EmailMessage()
    email['Subject'] = 'Thanks for registration'
    email['From'] = login
    email['To'] = 'yura.voskanyan.2003@mail.ru'
    email.set_content('Test message')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(login, password)
        server.send_message(email)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")
        send_message(user.email)
    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
import os
import smtplib
from email.message import EmailMessage
from typing import Optional

from db.database import get_user_db
from db.models import User
from dotenv import load_dotenv
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin

load_dotenv()

SECRET = os.getenv('SECRET_AUTH_KEY')

login = os.getenv("EMAIL_LOGIN")
password = os.getenv('EMAIL_PASSWORD')


def send_message(user_email: str) -> None:
    email = EmailMessage()
    email['Subject'] = 'Thanks for registration'
    email['From'] = login
    email['To'] = user_email
    HTML = f"<div><h1 style=\"text-align: center\">Hello, {user_email}!</h1><h1>We are pleased to welcome you to our project, where we help novice developers connect with experienced mentors to improve their knowledge in a certain area</h1></div>"
    email.set_content(HTML, subtype='html')

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

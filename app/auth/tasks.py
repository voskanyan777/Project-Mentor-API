import os
import smtplib
from email.message import EmailMessage

from celery import Celery
from dotenv import load_dotenv

load_dotenv()

login = os.getenv("EMAIL_LOGIN")
password = os.getenv('EMAIL_PASSWORD')

celery = Celery('tasks', broker='redis://localhost:6379')


@celery.task
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

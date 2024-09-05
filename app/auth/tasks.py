import os

from celery import Celery
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

load_dotenv()

login = os.getenv("EMAIL_LOGIN")
password = os.getenv('EMAIL_PASSWORD')

celery = Celery('tasks', broker='redis://localhost:6379')


@celery.task(name='app.auth.tasks.send_message')
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


@celery.task(name='app.auth.tasks.send_verify_email')
def send_verify_email(user_email: str, verify_token: str) -> None:
    email = EmailMessage()
    email['Subject'] = "Please verify your account"
    email['From'] = login
    email['To'] = user_email
    
    HTML = f"""
    <html>
    <head>
    </head>
    <body>
        <h1 style="text-align: center">Dear {user_email}, please verify your account</h1>
        <a href="https://site.com/verify?token={verify_token}">Verify</a>
    </body>
    </html>
    """
    
    email.set_content(HTML, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(login, password)
        server.send_message(email)

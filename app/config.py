import os
from dotenv import load_dotenv

load_dotenv()

SECRET_AUTH_KEY = os.environ.get('SECRET_AUTH_KEY')
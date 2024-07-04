from datetime import timedelta
import os
from dotenv import load_dotenv
from fastapi_login import LoginManager

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_AUTH_KEY')

manager = LoginManager(
    secret=SECRET_KEY,
    token_url='auth/login',
    default_expiry=timedelta(minutes=60),
)

fake_db = {
    'users':{
        'johndoe@mail.com':{
            'name': 'John doe',
            'password': 'hunter2'
        }
    }
}

@manager.user_loader()
async def query_user(user_id: str) -> dict:
    return fake_db["users"].get(user_id)
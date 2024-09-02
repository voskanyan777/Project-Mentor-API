import os
from dotenv import load_dotenv
from fastapi_users.authentication import JWTStrategy, BearerTransport, AuthenticationBackend
from fastapi_users import FastAPIUsers
from .manager import get_user_manager
from db.models import User

load_dotenv()

SECRET = os.getenv('SECRET_AUTH_KEY')

bearer_transport = BearerTransport(tokenUrl='auth/v1/jwt/login')

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name='jwt',
    transport=bearer_transport,
    get_strategy=get_jwt_strategy
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager=get_user_manager,
    auth_backends=[auth_backend]
)

current_active_user = fastapi_users.current_user()
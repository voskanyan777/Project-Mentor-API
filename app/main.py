import uuid
from fastapi_users import FastAPIUsers
from fastapi import FastAPI
from db.models import User
from auth.manager import get_user_manager
from auth.config import auth_backend
from auth.schemas import UserRead, UserCreate, UserUpdate


app = FastAPI()

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager=get_user_manager,
    auth_backends=[auth_backend]
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/v1/jwt',
    tags=['auth']
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth/v1',
    tags=['auth']
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

@app.get('/')
async def test():
    return 'root'
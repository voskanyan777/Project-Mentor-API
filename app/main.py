import uuid
from fastapi_users import FastAPIUsers
from fastapi import FastAPI, Depends
from db.models import User
from auth.manager import get_user_manager
from auth.config import auth_backend
from auth.schemas import UserRead, UserCreate, UserUpdate
from db.orm import AsyncOrm

app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager=get_user_manager,
    auth_backends=[auth_backend]
)

current_active_user = fastapi_users.current_user()

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

# @app.on_event("startup")
# async def startup():
#     async_orm = AsyncOrm()
#     await async_orm.create_tables()

@app.get('/protected')
async def test(user: User = Depends(current_active_user)):
    return {
        'data': f'{user.email}'
    }

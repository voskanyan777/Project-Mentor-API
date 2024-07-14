from fastapi import FastAPI, Depends
from db.models import User
from auth.config import auth_backend
from auth.schemas import UserRead, UserCreate
from routers.profile import profile_router
from auth.config import fastapi_users, current_active_user
app = FastAPI()



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
app.include_router(profile_router)

# `@app.on_event("startup")
# async def startup():
#     async_orm = AsyncOrm()
#     await async_orm.create_tables()`

@app.get('/protected/users_info')
async def test(user: User = Depends(current_active_user)):
    return {
        'user_id': user.id,
        'email': user.email,
        'login': user.login,
        'role': user.role,
    }

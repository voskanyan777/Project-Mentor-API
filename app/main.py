from fastapi import FastAPI, Depends
from db.models import User
from auth.config import auth_backend
from auth.schemas import UserRead, UserCreate
from routers.profile import profile_router
from routers.meeting import meeting_router
from routers.review import review_router
from auth.config import fastapi_users, current_active_user
from db.orm import AsyncOrm


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
app.include_router(meeting_router)
app.include_router(review_router)



# @app.on_event("startup")
# async def startup():
#     #
#     async_orm = AsyncOrm()
#     await async_orm.create_tables()

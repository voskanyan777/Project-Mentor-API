from fastapi import APIRouter, Depends
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select

from .config import query_user, manager
from .models import UserCreate
from db.database import get_async_session
from db.models import User

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@auth_router.post('/v1/login')
async def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = await query_user(email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )
    elif password != user['password']:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    access_token = manager.create_access_token(data={'sub': email})
    return {
        'access_token': access_token,
    }


@auth_router.get('/protected')
async def test_protected(user=Depends(manager)):
    return {
        'user': user
    }


@auth_router.post('/v1/register', status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate, session=Depends(get_async_session)):
    query = select(User).where(User.user_email == user.user_email)
    result = await session.scalar(query)
    if result is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    user = User(
        user_login=user.user_login,
        user_name=user.user_name,
        user_surname=user.user_surname,
        user_email=user.user_email,
        hashed_password=user.password.encode('UTF-8'),
        user_role=user.user_role
    )
    session.add(user)
    await session.commit()
    return {
        'ok': True
    }

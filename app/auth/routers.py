from fastapi import APIRouter, Depends
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .config import query_user, manager

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@auth_router.post('/login')
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
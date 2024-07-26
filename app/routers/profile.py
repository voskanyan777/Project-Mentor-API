from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import update

from db.models import User
from auth.config import current_active_user
from db.models import Profile, User
from db.database import get_async_session

class CreateProfile(BaseModel):
    bio: str
    experience: int
    specialization: str
    photo_url: str

profile_router = APIRouter(
    prefix="/profile",
    tags=["profile"],
)



@profile_router.post("/v1/add_profile")
async def add_profile(profile_info: CreateProfile, 
                      user: User = Depends(current_active_user), 
                      session = Depends(get_async_session)) -> dict:
    profile = Profile(user_id=user.id,
                      bio=profile_info.bio,
                      experience=profile_info.experience,
                      specialization=profile_info.specialization,
                      photo_url=profile_info.photo_url)
    session.add(profile)
    await session.commit()
    return {
        'ok': True
    }

@profile_router.post('/v1/change_login')
async def change_user_login(user_login: str, 
                            user: User = Depends(current_active_user),
                              session = Depends(get_async_session)) -> dict:
    stmt = update(User).where(User.login == user.login).values(login=user_login)
    await session.execute(stmt)
    await session.commit()
    return {
        'ok': True
    }
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import update, select
from sqlalchemy.exc import IntegrityError
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
    try:
        await session.execute(stmt)
        await session.commit()
        return {
            'ok': True
        }
    
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=400,
            detail='This login already exists'
        )

@profile_router.get('/v1/user_profiles')
async def get_user_profiles(session = Depends(get_async_session)) -> dict:
    query = select(
        User.login, User.email, User.role, Profile.experience,
          Profile.specialization, Profile.photo_url).join(Profile, User.id == Profile.user_id).where(User.role == 'user')
    result = (await session.execute(query)).all()
    result_dict = dict()
    for data in result:
        result_dict[data[0]] = dict()
        result_dict[data[0]]['login'] = data[0]
        result_dict[data[0]]['email'] = data[1]
        result_dict[data[0]]['experience'] = data[3]
        result_dict[data[0]]['specialization'] = data[4]
        result_dict[data[0]]['photo_url'] = data[5]
    return {
        'data': result_dict,
        'ok': True
    }

@profile_router.get('/v1/mentor_profiles')
async def get_mentor_profiles(session = Depends(get_async_session)) -> dict:
    query = select(
    User.login, User.email, User.role, Profile.experience,
        Profile.specialization, Profile.photo_url).join(Profile, User.id == Profile.user_id).where(User.role == 'mentor')
    result = (await session.execute(query)).all()
    result_dict = dict()
    for data in result:
        result_dict[data[0]] = dict()
        result_dict[data[0]]['login'] = data[0]
        result_dict[data[0]]['email'] = data[1]
        result_dict[data[0]]['experience'] = data[3]
        result_dict[data[0]]['specialization'] = data[4]
        result_dict[data[0]]['photo_url'] = data[5]
    return {
        'data': result_dict,
        'ok': True
    }
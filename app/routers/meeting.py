from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from auth.config import current_active_user
from db.models import Meeting, User
from db.database import get_async_session

meeting_router = APIRouter(
    prefix='/meeting',
    tags=['meeting']
)


class CreateMeeting(BaseModel):
    mentor_login: str
    description: str
    start_time: str


@meeting_router.post('/v1/create_meetings')
async def create_meetings(meetings_info: CreateMeeting,
                          session=Depends(get_async_session), 
                          user: User = Depends(current_active_user)) -> dict:
    # checking for user existence
    query = select(User.login).where(User.login == meetings_info.mentor_login)
    result = (await session.execute(query)).all()
    if not result:
        raise HTTPException(
            status_code=400,
            detail='Given user not exists'
            )
    meeting = Meeting(
        user_login=user.login,
        mentor_login=meetings_info.mentor_login,
        description=meetings_info.description,
        start_time=meetings_info.start_time
        )
    session.add_all([meeting])
    await session.commit()
    return {
        'data': None,
        'ok': True,
        'detail': None
    }

@meeting_router.get('/v1/meetings')
async def get_meetings(user: User=Depends(current_active_user), session=Depends(get_async_session)) -> dict:
    query = select(Meeting).where(Meeting.mentor_login == user.login)
    result = (await session.execute(query)).all()
    if not result:
        return {
            'data': None,
            'ok': True,
            'detail': None
        }
    result_dict = dict()
    for index, item in enumerate(result):
        item = item[0]
        result_dict[item.id] = {
            'id': index + 1,
            'user': item.user_login,
            'description': item.description,
            'start time': item.start_time
        }
    return {
        'data': result_dict,
        'ok': True,
        'detail': None
    }
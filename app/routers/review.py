from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy import select
from db.models import User, Review
from db.database import get_async_session
from auth.config import current_active_user
from .dependencies import verify_user

review_router = APIRouter(
    prefix='/review',
    tags=['review']
)

class UserReview(BaseModel):
    mentor_login: str
    rating: int = Field(le=5, ge=0)
    comment: str = Field(max_length=250)


@review_router.post('/v1/create_reviews')
async def create_review(user_review: UserReview, user: User=Depends(verify_user),
                        session=Depends(get_async_session)) -> dict:
    review = Review(
        review_login=user.login,
        mentor_login=user_review.mentor_login,
        rating=user_review.rating,
        comment=user_review.comment
    )
    session.add(review)
    await session.commit()
    return {
        'data': None,
        'ok': True,
        'detail': 'Review created'
    }

@review_router.get('/v1/reviews')
async def get_user_reviews(user: User=Depends(current_active_user),
                           session=Depends(get_async_session)) -> dict:
    if user.role == 'Mentor':
        query = select(Review).where(Review.mentor_login == user.login)
    else:
        query = select(Review).where(Review.user_login == user.login)
    result = (await session.execute(query)).all()
    if not result:
        return {
            'data': None,
            'ok': True,
            'detail': 'No reviews'
        }
    result_dict = dict()
    for index, item in enumerate(result):
        item = item[0]
        result_dict[item.id] = {
            'id': index + 1,
            'review_login': item.review_login,
            'mentor_login': item.mentor_login,
            'rating': item.rating,
            'comment': item.comment 
        }
    return {
        'data': result_dict,
        'ok': True,
        'detail': None
    }
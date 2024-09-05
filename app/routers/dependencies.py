from fastapi import Depends, HTTPException, status
from db.models import User
from auth.config import current_active_user

async def verify_user(user: User = Depends(current_active_user)) -> User:
    if not user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You're not verified"
        )
    return user
from enum import Enum
from typing import Annotated

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

intpk = Annotated[int, mapped_column(primary_key=True)]


# Base class for models
class Base(DeclarativeBase):
    pass


class UserRole(Enum):
    USER = 'User'
    MENTOR = 'Mentor'


class User(Base):
    __tablename__ = 'users'
    id: Mapped[intpk]
    user_login: Mapped[str] = mapped_column(String(40), nullable=False, unique=True)
    user_name: Mapped[str] = mapped_column(String(40), nullable=False)
    user_surname: Mapped[str] = mapped_column(String(40), nullable=False)
    user_email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    hashed_password: Mapped[bytes] = mapped_column(nullable=False)
    user_role: Mapped[str] = mapped_column(String(6), nullable=False, default='User')

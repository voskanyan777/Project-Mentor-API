from typing import Annotated, AsyncGenerator
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyBaseUserTable
from sqlalchemy import String, ForeignKey, CheckConstraint, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

intpk = Annotated[int, mapped_column(primary_key=True)]


# Base class for models
class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

class Test(Base):
    __tablename__ = 'test'
    id: Mapped[intpk]
    some_row: Mapped[str] = mapped_column(String(30), nullable=False)


# class User(Base):
#     __tablename__ = 'users'
#     __table_args__ = (CheckConstraint(
#         "user_role in ('user', 'mentor')"
#     ),)
#     id: Mapped[intpk]
#     user_login: Mapped[str] = mapped_column(String(40), nullable=False, unique=True)
#     user_name: Mapped[str] = mapped_column(String(40), nullable=False)
#     user_surname: Mapped[str] = mapped_column(String(40), nullable=False)
#     user_email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
#     hashed_password: Mapped[bytes] = mapped_column(nullable=False)
#     user_role: Mapped[str] = mapped_column(String(6), nullable=False, default='User')


# class Profile(Base):
#     __tablename__ = 'profile'
#     id: Mapped[intpk]
#     user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
#     bio: Mapped[str] = mapped_column(String(255))
#     experience: Mapped[int]
#     specialization: Mapped[str] = mapped_column(String(40), nullable=False)
#     photo_url: Mapped[str] = mapped_column(String(255))
#
#
# class Session(Base):
#     __tablename__ = 'session'
#     __table_args__ = (CheckConstraint(
#         "status in ('planned', 'carried out', 'canceled')"
#     ),)
#     id: Mapped[intpk]
#     teacher_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
#     student_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
#     topic: Mapped[str] = mapped_column(String(90), nullable=False)
#     status: Mapped[str] = mapped_column(String(15), nullable=False)
#
# class Review(Base):
#     __tablename__ = 'review'
#     __table_args__ = (CheckConstraint(
#         'rating in (1, 2, 3, 4, 5)'
#     ),)
#     id: Mapped[intpk]
#     session_id: Mapped[int] = mapped_column(ForeignKey('sessions.id'))
#     reviewr_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
#     rating: Mapped[int] = mapped_column(nullable=False)
#     comment: Mapped[str] = mapped_column(String(350))

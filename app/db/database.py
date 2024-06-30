from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from config import settings

async_engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True
)

async_session_maker = sessionmaker(engine=async_engine, class_=AsyncSession)


async def get_async_session():
    async with async_session_maker() as session:
        yield session()

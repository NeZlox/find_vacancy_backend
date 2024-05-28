
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.pool import NullPool

from src.config import settings

DATABASE_URL = settings.DATABASE_URL



#poolclass=NullPool,
async_engine = create_async_engine(url=DATABASE_URL, pool_size=5, max_overflow=10)#, echo=True)

async_session_maker = sessionmaker(bind=async_engine, autocommit=False, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):

    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        """Relationships не используются в repr(), т.к. могут вести к неожиданным подгрузкам"""
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"
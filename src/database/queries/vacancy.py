from typing import List

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload

from src.database.base_DAO import BaseDAO
from src.database.models import vacanciesModel
from src.database.schemas import Vacancy_CreateSchema, Vacancy_UpdateSchema
from src.exceptions import RequestHandlingError

__all__ = ['Vacancy_Query']


class Vacancy_Query(BaseDAO[vacanciesModel,Vacancy_CreateSchema, Vacancy_UpdateSchema]):
    model = vacanciesModel

    @classmethod
    async def select_all(cls) -> List[vacanciesModel]:
        async with cls.async_session_maker() as session:
            try:
                query = (
                    select(vacanciesModel)
                    .options(selectinload(vacanciesModel.skills), selectinload(vacanciesModel.url))
                )

                result_orm = await session.execute(query)
                result = result_orm.scalars().all()
                return result


            except (SQLAlchemyError, Exception) as e:
                await session.rollback()
                raise RequestHandlingError


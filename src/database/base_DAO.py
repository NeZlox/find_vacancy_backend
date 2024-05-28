from typing import Any, Dict, Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel
from sqlalchemy import asc, delete, desc, insert, select, update
from sqlalchemy.exc import SQLAlchemyError

from src.database.database import Base
from src.database.database import async_session_maker as sessionmaker
from src.exceptions import RequestHandlingError

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseDAO(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    model = None
    async_session_maker = sessionmaker

    @classmethod
    async def create_sortirovka(cls, sort: Dict[str, str]):
        order_by_clause = []
        for field, direction in sort.items():
            if direction == 'asc':
                order_by_clause.append(asc(getattr(cls.model, field)))
            elif direction == 'desc':
                order_by_clause.append(desc(getattr(cls.model, field)))

        return order_by_clause



    @classmethod
    async def find_one_or_none(cls, **filter_by) -> Optional[ModelType] | None:

        async with cls.async_session_maker() as session:
            try:
                stmt = select(cls.model).filter_by(**filter_by)
                result = await session.execute(stmt)

                return result.scalars().one_or_none()

            except (SQLAlchemyError, Exception) as e:
                await session.rollback()
                raise RequestHandlingError


    @classmethod
    async def find_all(cls, **filter_by) -> List[ModelType]:
        async with cls.async_session_maker() as session:
            try:
                query = select(cls.model.__table__.columns).where(**filter_by)
                result_orm = await session.execute(query)
                result = result_orm.mappings().all()

                return result


            except (SQLAlchemyError, Exception) as e:
                await session.rollback()
                raise RequestHandlingError


    @classmethod
    async def insert_one(cls,obj_in: Union[BaseModel,Dict[str, Any]]) -> Optional[ModelType]:
        if isinstance(obj_in, dict):
            create_data = obj_in
        else:
            create_data = obj_in.model_dump(exclude_unset=True)

        async with cls.async_session_maker() as session:
            try:
                stmt = insert(cls.model).values(**create_data).returning(cls.model.__table__.columns)
                result = await session.execute(stmt)
                await session.commit()
                return_result = result.mappings().first()
                return return_result

            except (SQLAlchemyError, Exception) as e:
                await session.rollback()
                raise RequestHandlingError


    @classmethod
    async def update(cls,id:int, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> Optional[ModelType]:



        if isinstance(obj_in, dict):
            update_data = obj_in
            update_data.pop("id", None)
        else:
            update_data = obj_in.model_dump(exclude_unset=True, exclude={'id'})

        async with cls.async_session_maker() as session:
            try:
                stmt = (
                    update(cls.model)
                    .where(cls.model.id == id)
                    .values(**update_data)
                    .returning(cls.model)
                )

                result = await session.execute(stmt)

                await session.commit()

                return result.scalars().one()

            except (SQLAlchemyError, Exception) as e:
                await session.rollback()
                raise RequestHandlingError



    @classmethod
    async def delete(cls, **filter_by) -> bool:
        async with cls.async_session_maker() as session:
            try:
                stmt = delete(cls.model).filter_by(**filter_by)
                result = await session.execute(stmt)
                if result.rowcount == 0:
                    await session.rollback()
                    return False

                await session.commit()

                return True


            except (SQLAlchemyError, Exception) as e:
                await session.rollback()
                raise RequestHandlingError
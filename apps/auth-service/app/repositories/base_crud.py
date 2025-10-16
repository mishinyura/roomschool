from abc import abstractmethod, ABC
from typing import Any

from sqlalchemy import select, delete as orm_delete, update as orm_update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import selectinload

from app.core.exceptions import DBError, DBDuplicateError, ObjectNotFoundError


class AbstractCrud(ABC):
    @abstractmethod
    async def get(self, obj_id: int, session: AsyncSession) -> Any: ...

    @abstractmethod
    async def create(self, obj: Any, session: AsyncSession) -> Any: ...

    @abstractmethod
    async def delete(self, obj_id: int, session: AsyncSession) -> Any: ...

    @abstractmethod
    async def update(self, obj_id: int, fields: dict, session: AsyncSession) -> Any: ...


class BaseCrud(AbstractCrud):
    def __init__(self, model):
        self.model = model

    async def get(self, obj_id: int, session: AsyncSession) -> Any:
        try:
            obj = await session.execute(select(self.model).where(self.model.id == obj_id))
        except SQLAlchemyError:
            raise DBError
        else:
            return obj.scalar_one_or_none()

    async def create(self, obj: Any, session: AsyncSession) -> Any:
        try:
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
        except IntegrityError as ex:
            await session.rollback()
            raise DBDuplicateError
        else:
            return obj

    async def delete(self, obj_id: int, session: AsyncSession) -> None:
        try:
            result = await session.execute(orm_delete(self.model).where(self.model.id == obj_id))
            if result.rowcount == 0:
                raise ObjectNotFoundError
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
            raise DBError

    async def update(self, obj_id: int, fields: dict, session: AsyncSession) -> None:
        try:
            await session.execute(orm_update(self.model).where(self.model.id == obj_id).values(**fields))
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
            raise DBError
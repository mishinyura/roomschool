from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from pydantic import BaseModel

from app.core.exceptions import ObjectNotFoundError


class BaseService:
    model = None
    crud = None
    eager_relations: list[str] = []

    def __init__(self):
        if not self.model or not self.crud:
            raise ValueError(f"{self.__class__.__name__} must define 'model' and 'crud'")

    async def _load_relations(self, obj_or_id, session: AsyncSession):
        """Подгружает связи, указанные в eager_relations"""
        if not self.eager_relations:
            # если связей нет, просто возвращаем объект как есть
            if isinstance(obj_or_id, self.model):
                return obj_or_id
            return await self.crud.get(obj_id=obj_or_id, session=session)

        stmt = select(self.model)
        for rel in self.eager_relations:
            stmt = stmt.options(selectinload(getattr(self.model, rel)))

        # если пришёл объект — достаём его id
        obj_id = obj_or_id.id if isinstance(obj_or_id, self.model) else obj_or_id
        stmt = stmt.where(self.model.id == obj_id)

        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_obj_by_id(self, obj_id: int, session: AsyncSession) -> object:
        obj = await self.crud.get(obj_id=obj_id, session=session)

        if not obj:
            raise ObjectNotFoundError
        return obj

    async def create_new_obj(self, data_obj: BaseModel, session: AsyncSession) -> object:
        obj = self.model(**data_obj.model_dump(exclude_unset=True))
        create_obj = await self.crud.create(obj=obj, session=session)
        return await self._load_relations(create_obj, session)

    async def delete_obj(self, obj_id: int, session: AsyncSession) -> None:
        await self.crud.delete(obj_id=obj_id, session=session)

    async def update_obj(self, obj_id: int, data_obj: BaseModel, session: AsyncSession) -> None:
        await self.crud.update(obj_id=obj_id, fields=data_obj.model_dump(exclude_unset=True), session=session)
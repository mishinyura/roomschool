from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from app.core.exceptions import ObjectNotFoundError


class BaseService:
    model = None
    crud = None
    eager_relations: list[str] = []

    def __init__(self):
        if not self.model or not self.crud:
            raise ValueError(f"{self.__class__.__name__} must define 'model' and 'crud'")

    async def get_obj_by_id(self, obj_id: int, session: AsyncSession) -> object:
        obj = await self.crud.get(obj_id=obj_id, session=session)

        if not obj:
            raise ObjectNotFoundError
        return obj

    async def create_new_obj(self, data_obj: BaseModel, session: AsyncSession) -> object:
        obj = self.model(**data_obj.model_dump(exclude_unset=True))
        create_obj = await self.crud.create(obj=obj, session=session)
        serialaze_obj = await self.crud.get(create_obj.id, session)
        # if self.eager_relations:
        #     serialaze_obj = await self.crud.get_with_relations(create_obj.id, session, self.eager_relations)
        #     return serialaze_obj
        # return create_obj
        return serialaze_obj

    async def delete_obj(self, obj_id: int, session: AsyncSession) -> None:
        await self.crud.delete(obj_id=obj_id, session=session)

    async def update_obj(self, obj_id: int, data_obj: BaseModel, session: AsyncSession) -> None:
        await self.crud.update(obj_id=obj_id, fields=data_obj.model_dump(exclude_unset=True), session=session)
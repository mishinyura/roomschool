from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import CityCreateSchema, CityUpdateSchema
from app.core.exceptions import DBError, DuplicateError, DBDuplicateError
from app.repositories import city_crud
from app.models import CityModel


class CityService:
    def __init__(self):
        self.crud = city_crud

    async def create_new_city(self, city_data: CityCreateSchema, session: AsyncSession) -> int:
        city = CityModel(
            name=city_data.name,
            time_zone=city_data.time_zone
        )
        try:
            city_id = await self.crud.create(obj=city, session=session)
        except DBDuplicateError:
            raise DuplicateError
        else:
            return city_id

    async def delete_city(self, city_id: int, session: AsyncSession) -> bool:
        try:
            await self.crud.delete(obj_id=city_id, session=session)
        except DBError:
            return False
        else:
            return True

    async def update_city(self, city_id: int, city_data: CityUpdateSchema, session: AsyncSession) -> bool:
        try:
            await self.crud.update(obj_id=city_id, fields=city_data.model_dump(exclude_unset=True), session=session)
        except DBError:
            return False
        else:
            return True

city_service = CityService()
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import CityCreateSchema
from app.core.exceptions import DBError, DuplicateError
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
            city_id = await self.crud.create(city=city, session=session)
        except DBError:
            raise DuplicateError
        else:
            return city_id


city_service = CityService()
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from app.models import CityModel
from app.core.exceptions import DBError


class CityCrud:
    async def create(self, city: CityModel, session: AsyncSession) -> int:
        try:
            session.add(city)
            await session.commit()
            await session.refresh(city)
        except SQLAlchemyError:
            await session.rollback()
            raise DBError
        else:
            return city.id

city_crud = CityCrud()
from sqlalchemy import select, delete as orm_delete, update as orm_update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from app.models import CityModel
from app.core.exceptions import DBError
from app.schemas import CityUpdateSchema
from app.repositories.base_crud import BaseCrud


class CityCrud(BaseCrud):
    def __init__(self):
        super().__init__(CityModel)


city_crud = CityCrud()
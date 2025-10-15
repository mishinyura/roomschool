from app.repositories import city_crud
from app.models import CityModel
from app.services.base_service import BaseService


class CityService(BaseService):
    crud = city_crud
    model = CityModel


city_service = CityService()
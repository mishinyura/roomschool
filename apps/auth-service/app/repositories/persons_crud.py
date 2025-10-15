from app.models import CityModel
from app.repositories.base_crud import BaseCrud


class PersonCrud(BaseCrud):
    def __init__(self):
        super().__init__(CityModel)


person_crud = PersonCrud()
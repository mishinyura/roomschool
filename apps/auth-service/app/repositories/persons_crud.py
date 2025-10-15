from app.models import PersonModel
from app.repositories.base_crud import BaseCrud


class PersonCrud(BaseCrud):
    def __init__(self):
        super().__init__(PersonModel)


person_crud = PersonCrud()
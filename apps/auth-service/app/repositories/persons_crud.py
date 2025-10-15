from app.models import PersonModel
from app.repositories.base_crud import BaseCrud


class PersonCrud(BaseCrud):
    def __init__(self):
        super().__init__(PersonModel)


    # async def get_by_uuid


person_crud = PersonCrud()
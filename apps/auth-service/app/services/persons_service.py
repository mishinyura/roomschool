from app.repositories import person_crud
from app.models import PersonModel
from app.services.base_service import BaseService


class PersonService(BaseService):
    crud = person_crud
    model = PersonModel


person_service = PersonService()
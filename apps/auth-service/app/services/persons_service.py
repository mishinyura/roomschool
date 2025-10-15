from app.repositories import person_crud
from app.models import PersonModel
from app.services.base_service import BaseService


class PersonService(BaseService):
    crud = person_crud
    model = PersonModel
    eager_relations = ["registration_address", "residential_address"]


person_service = PersonService()
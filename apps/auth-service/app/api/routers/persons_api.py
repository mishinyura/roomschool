from fastapi import APIRouter

from app.schemas import PersonOutClientSchema, PersonUpdateSchema, PersonCreateSchema
from app.services import person_service

from app.api.mixins import CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin


class PersonAPI(RetrieveMixin, CreateMixin, UpdateMixin, DeleteMixin):
    router = APIRouter()
    service = person_service
    create_schema = PersonCreateSchema
    update_schema = PersonUpdateSchema
    response_schema = PersonOutClientSchema


person_api = PersonAPI()
from fastapi import APIRouter, Request

from app.schemas import PersonOutClientSchema, PersonUpdateSchema, PersonCreateSchema
from app.services import person_service

from app.api.mixins import CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin


class PersonAPI(RetrieveMixin, CreateMixin, UpdateMixin, DeleteMixin):
    router = APIRouter()
    service = person_service
    create_schema = PersonCreateSchema
    update_schema = PersonUpdateSchema
    response_schema = PersonOutClientSchema

    def __init__(self):
        self.router.add_api_route('/profile', self.get_info_about_me, methods=['get'])

    async def get_info_about_me(self, request: Request):
        try:
            result = await self.service.crud.get()
        except:
            pass


person_api = PersonAPI()
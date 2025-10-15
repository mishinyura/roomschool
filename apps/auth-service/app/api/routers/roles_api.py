from fastapi import APIRouter

from app.services import role_service
from app.schemas import RoleCreateSchema, RoleUpdateSchema, RoleOutClientSchema

from app.api.mixins import CreateMixin, RetrieveMixin, DeleteMixin, UpdateMixin


class RoleAPI(RetrieveMixin, CreateMixin, DeleteMixin, UpdateMixin):
    router = APIRouter()
    service = role_service
    response_schema = RoleOutClientSchema
    create_schema = RoleCreateSchema
    update_schema = RoleUpdateSchema


role_api = RoleAPI()
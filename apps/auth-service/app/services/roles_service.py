from app.repositories import role_crud
from app.models import RoleModel
from app.services.base_service import BaseService


class RoleService(BaseService):
    crud = role_crud
    model = RoleModel


role_service = RoleService()
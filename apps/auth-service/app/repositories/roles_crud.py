from app.models import RoleModel
from app.repositories.base_crud import BaseCrud


class RoleCrud(BaseCrud):
    def __init__(self):
        super().__init__(RoleModel)


role_crud = RoleCrud()
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import role_crud
from app.models import RoleModel, AccountRoleModel
from app.services.base_service import BaseService
from app.schemas import  RoleAccountCreateSchema


class RoleService(BaseService):
    crud = role_crud
    model = RoleModel

    async def get_role_name_by_account(self, account_id: int, session: AsyncSession):
        role = await self.crud.get_by_account_id(account_id=account_id, session=session)
        return role.all()

    async def add_new_role_on_account(self, relation: RoleAccountCreateSchema, session: AsyncSession):
        role_account = AccountRoleModel(
            **relation.model_dump()
        )
        await self.crud.create(obj=role_account, session=session)

    async def remove_role_on_account(self, role_data: RoleAccountCreateSchema, session: AsyncSession):
        await self.crud.delete_by_account_id(account_id=role_data.account_id, role_id=role_data.role_id, session=session)


role_service = RoleService()
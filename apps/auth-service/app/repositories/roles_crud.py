from sqlalchemy import select, join, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from app.models import RoleModel, AccountRoleModel
from app.repositories.base_crud import BaseCrud
from app.core.exceptions import ObjectNotFoundError


class RoleCrud(BaseCrud):
    def __init__(self):
        super().__init__(RoleModel)

    async def get_by_account_id(self, account_id: int, session: AsyncSession):
        try:
            role = await session.execute(
                select(RoleModel)
                .join(AccountRoleModel, RoleModel.id == AccountRoleModel.role_id)
                .where(AccountRoleModel.account_id == account_id)
            )
        except:
            pass
        else:
            return role

    async def delete_by_account_id(self, account_id: int, role_id: int,  session: AsyncSession):
        try:
            await session.execute(
                delete(AccountRoleModel)
                .where((AccountRoleModel.account_id == account_id) & (AccountRoleModel.role_id == role_id))
            )
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
            raise ObjectNotFoundError




role_crud = RoleCrud()
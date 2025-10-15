from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import account_crud
from app.models import AccountModel
from app.services.base_service import BaseService
from app.schemas import AccountUpdateUsernameSchema, AccountUpdatePasswordSchema, AccountCreateSchema
from app.core.security import hash_password


class AccountService(BaseService):
    crud = account_crud
    model = AccountModel

    async def create_new_account(self, data: AccountCreateSchema, session: AsyncSession) -> AccountModel:
        obj = AccountModel(
            person_id=data.person_id,
            username=data.username,
            hash_password=hash_password(data.password)
        )
        new_obj = self.crud.create(obj=obj, session=session)
        return new_obj

    async def update_password_by_uuid(self, data: AccountUpdatePasswordSchema, session: AsyncSession) -> None:
        uuid = data.uuid
        update_fileds = {
            "hash_password": hash_password(data.password)
        }

        self.crud.update_by_uuid(uuid=uuid, fields=update_fileds, session=session)




account_service = AccountService()
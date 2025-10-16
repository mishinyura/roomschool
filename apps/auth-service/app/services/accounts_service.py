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

    async def get_account_by_uuid(self, uuid, session: AsyncSession):
        await self.crud.get_by_uuid(uuid=uuid, session=session)

    async def create_new_account(self, data: AccountCreateSchema, session: AsyncSession) -> AccountModel:
        obj = AccountModel(
            person_id=data.person_id,
            username=data.username,
            hash_password=hash_password(data.password)
        )
        print(obj, "OOO")
        new_obj = await self.crud.create(obj=obj, session=session)
        print(new_obj, "ККК")
        serialaze_obj = await self.crud.get(new_obj.id, session)
        print("EEE:", serialaze_obj)
        return serialaze_obj

    async def update_password_by_uuid(self, data: AccountUpdatePasswordSchema, session: AsyncSession) -> None:
        uuid = data.uuid
        new_hash_password = hash_password(data.new_password)
        print(new_hash_password, "OOL")
        account = await self.crud.get_by_uuid(uuid=uuid, session=session)

        if account.hash_password != new_hash_password:
            raise

        update_fileds = {
            "hash_password": new_hash_password
        }

        await self.crud.update_by_uuid(uuid=uuid, fields=update_fileds, session=session)


account_service = AccountService()
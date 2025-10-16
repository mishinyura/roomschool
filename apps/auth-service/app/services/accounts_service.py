from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import account_crud
from app.models import AccountModel
from app.services.base_service import BaseService
from app.schemas import AccountUpdateUsernameSchema, AccountUpdatePasswordSchema, AccountCreateSchema, AccountFullOutClientSchema, AccountLoginSchema
from app.core.security import hash_password


class AccountService(BaseService):
    crud = account_crud
    model = AccountModel

    async def get_account_by_uuid(self, uuid: str, session: AsyncSession):
        result = await self.crud.get_by_uuid(uuid, session)
        if not result:
            return None

        person_dict = {
            "first_name": result.get("first_name"),
            "last_name": result.get("last_name"),
            "middle_name": result.get("middle_name"),
            "gender": result.get("gender"),
            "birthday": result.get("birthday"),
            "phone": result.get("phone"),
            "email": result.get("email"),
            "registration_address": {
                "street": result.get("reg_street"),
                "house_number": result.get("reg_house"),
                "flat_number": result.get("reg_flat"),
                "city": result.get("reg_city_name")
            } if result.get("reg_street") else None,
            "residential_address": {
                "street": result.get("live_street"),
                "house_number": result.get("live_house"),
                "flat_number": result.get("live_flat"),
                "city": result.get("live_city_name")
            } if result.get("live_street") else None
        }

        account_dict = {
            "uuid": result.get("uuid"),
            "username": result.get("username"),
            "is_active": result.get("is_active"),
            "is_verified": result.get("is_verified"),
            "created_at": result.get("created_at"),
            "updated_at": result.get("updated_at"),
            "person": person_dict
        }

        print("RESULT SERVICE", account_dict)

        return AccountFullOutClientSchema.model_validate(account_dict).model_dump(mode='json')

    async def get_account_by_username(self, username: str, session: AsyncSession):
        account = await self.crud.get_by_username(username=username, session=session)
        return AccountLoginSchema.model_validate(account).model_dump(mode='json')

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
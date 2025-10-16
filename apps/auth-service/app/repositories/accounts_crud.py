import uuid as py_uuid

from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import AccountModel, PersonModel
from app.repositories.base_crud import BaseCrud
from app.core.exceptions import DBError


class AccountCrud(BaseCrud):
    def __init__(self):
        super().__init__(AccountModel)

    async def update_by_uuid(self, uuid: py_uuid, fields: dict, session: AsyncSession):
        try:
            await session.execute(update(AccountModel).where(AccountModel.uuid == uuid).values(**fields))
            await session.commit()
        except SQLAlchemyError:
            raise DBError

    async def get_by_uuid(self, uuid: str, session):
        stmt = (
            select(AccountModel)
            .where(AccountModel.uuid == uuid)
            .options(
                selectinload(AccountModel.account_person)
                .options(
                    selectinload(PersonModel.person_address_registration),
                    selectinload(PersonModel.person_address_living),
                )
            )
        )
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

        # try:
        #     print("RRR", uuid)
        #     account = await session.execute(select(AccountModel).where(AccountModel.uuid == uuid))
        #     print('OOK', account)
        # except SQLAlchemyError:
        #     raise DBError
        # else:
        #     return account


account_crud = AccountCrud()
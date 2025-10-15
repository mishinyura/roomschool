import uuid as py_uuid

from sqlalchemy import select, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import AccountModel
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


account_crud = AccountCrud()
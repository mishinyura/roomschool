import uuid as py_uuid

from sqlalchemy import select, update, text
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
        query = """
        SELECT 
            a.uuid,
            a.username,
            p.first_name,
            p.last_name,
            p.middle_name,
            p.gender,
            p.birthday,
            p.phone,
            p.email,
            reg.street AS reg_street,
            reg.house_number AS reg_house,
            reg.flat_number AS reg_flat,
            reg_city.name AS reg_city_name,
            live.street AS live_street,
            live.house_number AS live_house,
            live.flat_number AS live_flat,
            live_city.name AS live_city_name,
            a.is_active,
            a.is_verified,
            a.created_at,
            a.updated_at
        FROM accounts a
        JOIN persons p ON p.id = a.person_id
        LEFT JOIN addresses reg ON reg.id = p.registration_address_id
        LEFT JOIN cities reg_city ON reg_city.id = reg.city_id
        LEFT JOIN addresses live ON live.id = p.residential_address_id
        LEFT JOIN cities live_city ON live_city.id = live.city_id
        WHERE a.uuid = :uuid
        """
        result = await session.execute(text(query), {"uuid": uuid})
        row = result.mappings().first()
        print("BD Result: ", row)
        return row


account_crud = AccountCrud()
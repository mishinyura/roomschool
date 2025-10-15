from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import AddressUpdateSchema, AddressBaseSchema
from app.models import AddressModel
from app.repositories import address_crud
from app.core.exceptions import DBError, DuplicateError

from app.services.base_service import BaseService


class AddressService(BaseService):
    crud = address_crud
    model = AddressModel
    eager_relations = ["city"]
    # async def create_new_address(self, address_data: AddressBaseSchema, session: AsyncSession) -> int:
    #     address = AddressModel(
    #         city_id=address_data.city_id,
    #         street=address_data.street,
    #         house_number=address_data.house_number,
    #         flat_number=address_data.flat_number
    #     )
    #     try:
    #         address_id = await self.crud.create(obj=address, session=session)
    #     except DBError:
    #         raise DuplicateError
    #     else:
    #         return address_id
    #
    # async def delete_address(self, address_id: int, session: AsyncSession) -> bool:
    #     try:
    #         await self.crud.delete(obj_id=address_id, session=session)
    #     except DBError:
    #         return False
    #     else:
    #         return True
    #
    # async def update_address(self, address_id: int, address_data: AddressUpdateSchema, session: AsyncSession) -> bool:
    #     try:
    #         await self.crud.update(obj_id=address_id, fields=address_data.model_dump(exclude_unset=True), session=session)
    #     except DBError:
    #         return False
    #     else:
    #         return True


address_service = AddressService()
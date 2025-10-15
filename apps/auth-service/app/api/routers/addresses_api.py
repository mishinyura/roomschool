from fastapi import APIRouter

from app.services import address_service
from app.schemas.addresses_schema import AddressUpdateSchema, AddressBaseSchema, AddressOutClientSchema

from app.api.mixins import CreateMixin, RetrieveMixin, DeleteMixin, UpdateMixin


class AddressAPI(CreateMixin, DeleteMixin, UpdateMixin):
    router = APIRouter()
    service = address_service
    response_schema = AddressOutClientSchema
    create_schema = AddressBaseSchema
    update_schema = AddressUpdateSchema

    @router.get("/search")
    async def search_by_street(self, request: str):
        return await self.service.search_by_street(request)


address_api = AddressAPI()
address_api()
# address_api.register()

#Старая версия api
# @address_router.post("/")
# async def create_address(address_data: AddressBaseSchema, session: AsyncSession = Depends(get_session)):
#     try:
#         await address_service.create_new_address(address_data=address_data, session=session)
#     except DuplicateError as ex:
#         raise HTTPException(status_code=HTTP_409_CONFLICT, detail=str(ex))
#     else:
#         return Response(status_code=HTTP_201_CREATED)
#
#
# @address_router.delete('/{address_id}')
# async def delete_address(address_id: int, session: AsyncSession = Depends(get_session)):
#     result = await address_service.delete_address(address_id=address_id, session=session)
#
#     if not result:
#         raise HTTPException(status_code=HTTP_409_CONFLICT, detail="Error")
#     return Response(status_code=HTTP_204_NO_CONTENT)
#
#
# @address_router.patch('/{address_id}')
# async def delete_address(address_id: int, address_data: AddressUpdateSchema, session: AsyncSession = Depends(get_session)):
#     result = await address_service.update_address(address_id=address_id, address_data=address_data, session=session)
#
#     if not result:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Error")
#     return Response(status_code=HTTP_204_NO_CONTENT)
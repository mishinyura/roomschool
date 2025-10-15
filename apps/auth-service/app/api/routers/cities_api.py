from fastapi import APIRouter

from app.schemas import CityCreateSchema, CityUpdateSchema
from app.services import city_service

from app.api.mixins import CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin


class CityAPI(RetrieveMixin, CreateMixin, UpdateMixin, DeleteMixin):
    router = APIRouter()
    service = city_service
    create_schema = CityCreateSchema
    update_schema = CityUpdateSchema
    response_schema = CityCreateSchema


city_api = CityAPI()



#Старые ручки
# @city_router.post('/', dependencies=[Depends(user_validate.validate)])
# async def create_city(city_data: CityCreateSchema, session: AsyncSession = Depends(get_session)):
#     try:
#         await city_service.create_new_city(city_data=city_data, session=session)
#     except DuplicateError as ex:
#         raise HTTPException(status_code=HTTP_409_CONFLICT, detail=str(ex))
#     else:
#         return Response(status_code=HTTP_201_CREATED)
#
#
# @city_router.delete('/{city_id}', dependencies=[Depends(user_validate.validate)])
# async def delete_city(city_id: int, session: AsyncSession = Depends(get_session)):
#     result = await city_service.delete_city(city_id=city_id, session=session)
#
#     if not result:
#         raise HTTPException(status_code=HTTP_409_CONFLICT, detail="Error")
#     return Response(status_code=HTTP_204_NO_CONTENT)
#
#
# @city_router.patch('/{city_id}', dependencies=[Depends(user_validate.validate)])
# async def delete_city(city_id: int, city_data: CityUpdateSchema, session: AsyncSession = Depends(get_session)):
#     result = await city_service.update_city(city_id=city_id, city_data=city_data, session=session)
#
#     if not result:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Error")
#     return Response(status_code=HTTP_204_NO_CONTENT)
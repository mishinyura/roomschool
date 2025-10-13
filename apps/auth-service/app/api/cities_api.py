from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_201_CREATED, HTTP_409_CONFLICT, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from app.schemas import CityCreateSchema, CityUpdateSchema
from app.core.db import get_session
from app.services import city_service
from app.core.exceptions import DuplicateError
from app.core.validators import user_validate

city_router = APIRouter()


@city_router.post('/', dependencies=[Depends(user_validate.validate)])
async def create_city(city_data: CityCreateSchema, session: AsyncSession = Depends(get_session)):
    try:
        await city_service.create_new_city(city_data=city_data, session=session)
    except DuplicateError as ex:
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail=str(ex))
    else:
        return Response(status_code=HTTP_201_CREATED)


@city_router.delete('/{city_id}', dependencies=[Depends(user_validate.validate)])
async def delete_city(city_id: int, session: AsyncSession = Depends(get_session)):
    result = await city_service.delete_city(city_id=city_id, session=session)

    if not result:
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail="Error")
    return Response(status_code=HTTP_204_NO_CONTENT)


@city_router.patch('/{city_id}', dependencies=[Depends(user_validate.validate)])
async def delete_city(city_id: int, city_data: CityUpdateSchema, session: AsyncSession = Depends(get_session)):
    result = await city_service.update_city(city_id=city_id, city_data=city_data, session=session)

    if not result:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Error")
    return Response(status_code=HTTP_204_NO_CONTENT)
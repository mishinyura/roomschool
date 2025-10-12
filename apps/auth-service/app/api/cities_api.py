from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_201_CREATED, HTTP_409_CONFLICT

from app.schemas import CityCreateSchema
from app.core.db import get_session
from app.services import city_service
from app.core.exceptions import DuplicateError

city_router = APIRouter()


@city_router.post('/')
async def create_city(city_data: CityCreateSchema, session: AsyncSession = Depends(get_session)):
    try:
        await city_service.create_new_city(city_data=city_data, session=session)
    except DuplicateError as ex:
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail=str(ex))
    else:
        return Response(status_code=HTTP_201_CREATED)

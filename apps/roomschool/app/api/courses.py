from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_404_NOT_FOUND

from app.services import course_service
from app.core.exceptions import ObjectNotFoundError
from app.core.db import get_session
from app.schemas import CourseOutClientSchema

course_router = APIRouter()


@course_router.get('/{slug}', response_model=CourseOutClientSchema)
async def get_course(slug: str, session: AsyncSession = Depends(get_session)):
    try:
        course = await course_service.get_course_by_slug(slug=slug, session=session)
    except ObjectNotFoundError as ex:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=str(ex))
    else:
        return course

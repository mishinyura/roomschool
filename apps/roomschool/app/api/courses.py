from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_409_CONFLICT

from app.services import course_service
from app.core.exceptions import ObjectNotFoundError
from app.core.db import get_session
from app.schemas import CourseOutClientSchema, CourseInClientSchema, CourseUpdateSchema


course_router = APIRouter()


@course_router.get("/{slug}", response_model=CourseOutClientSchema)
async def get_course(slug: str, session: AsyncSession = Depends(get_session)):
    try:
        course = await course_service.get_course_by_slug(slug=slug, session=session)
    except ObjectNotFoundError as ex:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=str(ex))
    else:
        return course


@course_router.post("/")
async def create_course(
    course_data: CourseInClientSchema, session: AsyncSession = Depends(get_session)
):

    await course_service.create_new_course(course_data, session=session)

    return Response(status_code=HTTP_201_CREATED)


@course_router.patch("/")
async def update_course(course_data: CourseUpdateSchema, session: AsyncSession = Depends(get_session)
):
    result = await course_service.update_course(course_data, session=session)
    if not result:
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail="Conflict")

    return Response(status_code=HTTP_204_NO_CONTENT)
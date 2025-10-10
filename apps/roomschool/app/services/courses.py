from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import course_crud
from app.schemas import CourseOutClientSchema
from app.core.exceptions import ObjectNotFoundError


class CourseService():
    def __init__(self):
        self.crud = course_crud

    async def get_course_by_slug(self, slug: str, session: AsyncSession) -> CourseOutClientSchema:
        result = await self.crud.get_by_slug(slug=slug, session=session)

        if not result:
            raise ObjectNotFoundError

        return CourseOutClientSchema.model_validate(result, from_attributes=True)


course_service = CourseService()
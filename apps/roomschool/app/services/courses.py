from sqlalchemy.ext.asyncio import AsyncSession
from slugify import slugify

from app.repositories import course_crud
from app.schemas import CourseOutClientSchema, CourseInClientSchema, CourseUpdateSchema
from app.models import CourseModel
from app.core.exceptions import ObjectNotFoundError, SqlAlchemyError


class CourseService:
    def __init__(self):
        self.crud = course_crud

    async def get_course_by_slug(
        self, slug: str, session: AsyncSession
    ) -> CourseOutClientSchema:
        result = await self.crud.get_by_slug(slug=slug, session=session)

        if not result:
            raise ObjectNotFoundError

        return CourseOutClientSchema.model_validate(result, from_attributes=True)

    async def create_new_course(
        self, course_data: CourseInClientSchema, session: AsyncSession
    ) -> bool:
        course = CourseModel(
            slug=course_data.slug if course_data.slug else slugify(course_data.title),
            title=course_data.title,
            short_description=course_data.short_description,
            main_description=course_data.main_description,
            full_description=course_data.full_description,
            price=course_data.price,
            discount=course_data.discount,
            image=course_data.image,
            is_archived=course_data.is_archived,
        )
        try:
            await self.crud.create(course, session=session)
        except SqlAlchemyError:
            return False
        else:
            return True

    async def update_course(self, course_data: CourseUpdateSchema, session: AsyncSession) -> bool:
        try:
            await self.crud.update(course_data.id, course_data.fields, session)
        except SqlAlchemyError:
            return False
        else:
            return True


course_service = CourseService()

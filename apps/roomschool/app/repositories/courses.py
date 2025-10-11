from typing import Any

from sqlalchemy import select, update as orm_update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import SQLAlchemyError

from app.repositories import BaseRepo
from app.models import CourseModel
from app.core.exceptions import SqlAlchemyError


class CourseCrud(BaseRepo):
    async def get(self, course_id: int, session: AsyncSession) -> CourseModel | None:
        course = await session.execute(
            select(CourseModel).where(CourseModel.id == course_id)
        )

        return course.scalar_one_or_none()

    async def get_by_slug(self, slug: str, session: AsyncSession) -> CourseModel | None:
        course = await session.execute(
            select(CourseModel).where(CourseModel.slug == slug)
        )

        return course.scalar_one_or_none()

    async def create(self, course: CourseModel, session: AsyncSession) -> int:
        try:
            session.add(course)
            await session.commit()
            await session.refresh(course)
        except SQLAlchemyError:
            await session.rollback()
            raise SqlAlchemyError
        else:
            return course.id

    async def update(self, course_id: int, fields: dict, session: AsyncSession) -> None:
        try:
            await session.execute(
                orm_update(CourseModel)
                .where(CourseModel.id == course_id)
                .values(**fields)
            )
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
            raise SqlAlchemyError

    async def delete(self, course_id: int, session: AsyncSession) -> None:
        course = self.get(course_id, session)

        if not course:
            raise SqlAlchemyError
        try:
            await session.delete(course)
        except SQLAlchemyError:
            raise SqlAlchemyError


course_crud = CourseCrud()

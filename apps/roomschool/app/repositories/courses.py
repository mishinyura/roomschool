from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.repositories import BaseRepo
from app.models import CourseModel


class CourseCrud(BaseRepo):
    async def get(self, obj_id: int, session: AsyncSession) -> Any:
        pass

    async def get_by_slug(self, slug: str, session: AsyncSession) -> CourseModel | None:
        course = await session.execute(select(CourseModel).where(CourseModel.slug == slug))

        return course.scalar_one_or_none()
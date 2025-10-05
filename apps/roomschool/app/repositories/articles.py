from typing import Any, List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.db import get_session
from app.models import ArticleModel
from app.repositories import BaseRepo
from app.schemas import ArticleBase


class ArticleCrud(BaseRepo):
    async def get(self, post_id: int, session: AsyncSession) -> ArticleModel | None:
        result = await session.execute(
            select(ArticleModel)
            .where(ArticleModel.id == post_id)
            .options(selectinload(ArticleModel.author))
        )
        return result.scalar_one_or_none()

    async def get_by_slug(self, slug: str, session: AsyncSession) -> ArticleModel | None:
        result = await session.execute(
            select(ArticleModel)
            .where(ArticleModel.slug == slug)
            .options(selectinload(ArticleModel.author))
        )
        return result.scalar_one_or_none()

    async def get_all(self, session: AsyncSession) -> List[ArticleModel]:
        result = await session.execute(
            select(ArticleModel).options(selectinload(ArticleModel.author))
        )
        posts = result.scalars().all()

        return posts


post_crud = ArticleCrud()

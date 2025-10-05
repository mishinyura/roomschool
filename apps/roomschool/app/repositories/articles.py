from typing import Any, List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload

from app.models import ArticleModel
from app.repositories import BaseRepo
from app.schemas import ArticleBase
from app.core.exceptions import SqlAlchemyError


class ArticleCrud(BaseRepo):
    async def get(self, post_id: int, session: AsyncSession) -> ArticleModel | None:
        result = await session.execute(
            select(ArticleModel)
            .where(ArticleModel.id == post_id)
            .options(selectinload(ArticleModel.author))
        )
        return result.scalar_one_or_none()

    async def get_by_slug(
            self, slug: str, session: AsyncSession
    ) -> ArticleModel | None:
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

    async def create(self, article: ArticleBase, session: AsyncSession) -> None:
        print(article.__dict__)
        try:
            session.add(article)
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
            raise SqlAlchemyError


article_crud = ArticleCrud()

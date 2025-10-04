from typing import Any, List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.db import get_session
from app.models import PostsModel
from app.repositories import BaseRepo
from app.schemas import PostBase


class PostsCrud(BaseRepo):
    async def get(self, post_id: int, session: AsyncSession) -> PostBase | None:
        result = await session.execute(
            select(PostsModel)
            .where(PostsModel.id == post_id)
            .options(selectinload(PostsModel.author))
        )
        return result.scalar_one_or_none()

    async def get_by_slug(self, slug: str, session: AsyncSession) -> PostBase | None:
        result = await session.execute(
            select(PostsModel)
            .where(PostsModel.slug == slug)
            .options(selectinload(PostsModel.author))
        )
        print("DD", type(result))
        return result.scalar_one_or_none()

    async def get_all(self, session: AsyncSession) -> List:
        result = await session.execute(
            select(PostsModel).options(selectinload(PostsModel.author))
        )
        posts = result.scalars().all()

        return posts


post_crud = PostsCrud()

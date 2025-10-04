from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import PostNotFoundError
from app.repositories import post_crud
from app.schemas import PostBase, PostOutClient


class PostService:
    def __init__(self):
        self.crud = post_crud

    async def get_post_by_slug(self, slug: str, session: AsyncSession) -> PostOutClient:
        post = await self.crud.get_by_slug(slug=slug, session=session)

        if not post:
            raise PostNotFoundError

        print(post.__dict__)
        return PostOutClient.model_validate(post)

    async def get_all_posts(self, session: AsyncSession) -> List[PostBase]:
        posts = await self.crud.get_all(session)

        if not posts:
            return []
        return [PostBase.model_validate(posts) for posts in posts]


posts_service = PostService()

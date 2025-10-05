from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import PostNotFoundError
from app.repositories import post_crud
from app.schemas import ArticleBase, ArticleOutClient


class PostService:
    def __init__(self):
        self.crud = post_crud

    async def get_post_by_slug(self, slug: str, session: AsyncSession) -> ArticleOutClient:
        post = await self.crud.get_by_slug(slug=slug, session=session)

        if not post:
            raise PostNotFoundError

        print(post.__dict__)
        return ArticleOutClient.model_validate(post)

    async def get_all_posts(self, session: AsyncSession) -> List[ArticleOutClient]:
        posts = await self.crud.get_all(session)

        if not posts:
            return []
        return [ArticleOutClient.model_validate(posts) for posts in posts]


posts_service = PostService()

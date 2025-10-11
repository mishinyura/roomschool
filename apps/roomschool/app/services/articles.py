from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from slugify import slugify

from app.core.exceptions import PostNotFoundError, SqlAlchemyError
from app.repositories import article_crud
from app.schemas import ArticleBase, ArticleOutClient
from app.models import ArticleModel, AuthorModel
from app.services.authors import author_service


class ArticleServices:
    def __init__(self):
        self.crud = article_crud

    async def get_post_by_slug(
        self, slug: str, session: AsyncSession
    ) -> ArticleOutClient:
        post = await self.crud.get_by_slug(slug=slug, session=session)

        if not post:
            raise PostNotFoundError

        print(post.__dict__)
        return ArticleOutClient.model_validate(post, from_attributes=True)

    async def get_all_posts(self, session: AsyncSession) -> List[ArticleOutClient]:
        posts = await self.crud.get_all(session)

        if not posts:
            return []
        return [
            ArticleOutClient.model_validate(posts, from_attributes=True)
            for posts in posts
        ]

    async def add_new_article(self, article_data, session: AsyncSession) -> None:
        author_id = await author_service.add_new_author(
            article_data.author, session=session
        )

        article = ArticleModel(
            slug=slugify(article_data.title),
            title=article_data.title,
            description=article_data.description,
            author_id=author_id,
            is_archived=False,
        )

        try:
            await self.crud.create(article=article, session=session)
        except SqlAlchemyError:
            return None


article_services = ArticleServices()

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import author_crud
from app.models.authors import AuthorModel
from app.schemas import AuthorInClient
from app.core.exceptions import SqlAlchemyError


class AuthorServices:
    def __init__(self):
        self.crud = author_crud

    async def add_new_author(
        self, author_data: AuthorInClient, session: AsyncSession
    ) -> int:
        author = AuthorModel(
            name=author_data.name,
            post=author_data.post,
            image_url=author_data.image_url,
        )
        try:
            author_id = await self.crud.create(author=author, session=session)
        except SqlAlchemyError:
            return 0
        else:
            return author_id


author_service = AuthorServices()

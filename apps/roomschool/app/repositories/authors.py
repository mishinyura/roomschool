from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from app.repositories.base import BaseRepo
from app.models import AuthorModel
from app.core.exceptions import SqlAlchemyError


class AuthorCrud(BaseRepo):
    async def get(self, obj_id: int, session: AsyncSession) -> Any:
        pass

    async def create(self, author: AuthorModel, session: AsyncSession) -> int:
        try:
            session.add(author)
            await session.commit()
            await session.refresh(author)
        except SQLAlchemyError:
            await session.rollback()
            raise SqlAlchemyError
        else:
            return author.id

author_crud = AuthorCrud()
from abc import abstractmethod
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepo:
    @abstractmethod
    async def get(self, obj_id: int, session: AsyncSession) -> Any: ...

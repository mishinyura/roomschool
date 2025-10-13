from fastapi import APIRouter, Depends, HTTPException, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session


class CreateMixin:
    """Добавляет POST /"""
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "router") or not isinstance(cls.router, APIRouter):
            raise ValueError(f"{cls.__name__}: требуется cls.router = APIRouter(...)")

        if not hasattr(cls, "_service"):
            raise ValueError(f"{cls.__name__}: требуется _service для CreateMixin")

        @cls.router.post("/")
        async def create(data: cls._schemas["create"], session: AsyncSession = Depends(get_session)):
            obj_id = await cls._service.create_new_address(data, session)
            return {"id": obj_id}


class UpdateMixin:
    """Добавляет PATCH /{id}"""
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        @cls.router.patch("/{obj_id}")
        async def update(obj_id: int, data: cls._schemas["update"], session: AsyncSession = Depends(get_session)):
            updated = await cls._service.update(obj_id, data, session)
            if not updated:
                raise HTTPException(status_code=404, detail="Object not found")
            return Response(status_code=200)


class DeleteMixin:
    """Добавляет DELETE /{id}"""
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        @cls.router.delete("/{obj_id}")
        async def delete(obj_id: int, session: AsyncSession = Depends(get_session)):
            deleted = await cls._service.delete(obj_id, session)
            if not deleted:
                raise HTTPException(status_code=404, detail="Object not found")
            return Response(status_code=204)


class RetrieveMixin:
    """Добавляет GET /{id}"""
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        @cls.router.get("/{obj_id}")
        async def get(obj_id: int, session: AsyncSession = Depends(get_session)):
            obj = await cls._service.get(obj_id, session)
            if not obj:
                raise HTTPException(status_code=404, detail="Object not found")
            return obj
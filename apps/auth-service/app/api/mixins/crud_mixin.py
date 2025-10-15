from fastapi import Depends
from fastapi.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_201_CREATED
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.core.exceptions import DuplicateError, DBError

from app.api.mixins.base_mixin import BaseEndpointMixin


class CreateMixin(BaseEndpointMixin):
    """Добавляет POST /"""
    def __call__(self, *args, **kwargs):
        @self.router.post("/")
        async def create(data: self.create_schema, session: AsyncSession = Depends(get_session)):
            try:
                obj = await self.service.create_new_obj(data_obj=data, session=session)
            except DuplicateError as ex:
                self.conflict(detail=str(ex))
            else:
                return JSONResponse(
                    status_code=HTTP_201_CREATED,
                    content=self.response_schema.model_validate(obj, from_attributes=True).model_dump()
                )


class UpdateMixin(BaseEndpointMixin):
    """Добавляет PATCH /{id}"""
    def __call__(self):
        @self.router.patch("/{obj_id}")
        async def update(obj_id: int, data: self.update_schema, session: AsyncSession = Depends(get_session)):
            try:
                await self.service.update_obj(obj_id=obj_id, data_obj=data, session=session)
            except DBError:
                self.not_found()
            return JSONResponse(status_code=HTTP_200_OK, content={"message": "Updated"})


class DeleteMixin(BaseEndpointMixin):
    """Добавляет DELETE /{id}"""
    def __call__(self):
        @self.router.delete("/{obj_id}")
        async def delete(obj_id: int, session: AsyncSession = Depends(get_session)):
            try:
                await self.service.delete_obj(obj_id=obj_id, session=session)
            except DBError:
                self.not_found()
            return JSONResponse(status_code=HTTP_200_OK, content={"message": "Deleted"})


class RetrieveMixin(BaseEndpointMixin):
    """Добавляет GET /{id}"""
    def __call__(self):
        @self.router.get("/{obj_id}")
        async def get(obj_id: int, session: AsyncSession = Depends(get_session)):
            obj = await self.service.get_obj_by_id(obj_id=obj_id, session=session)
            if not obj:
                self.not_found(detail="Object not found")
            return self.response_schema.model_validate(obj, from_attributes=True)


# class CreateMixin(BaseEndpointMixin):
#     """Добавляет POST /"""
#     @classmethod
#     def register(cls):
#         @cls.router.post("/")
#         async def create(data: cls.create_schema, session: AsyncSession = Depends(get_session)):
#             try:
#                 obj = await cls.service.create_new_obj(data_obj=data, session=session)
#             except DuplicateError as ex:
#                 cls.conflict(detail=str(ex))
#             else:
#                 return JSONResponse(
#                     status_code=HTTP_201_CREATED,
#                     content=cls.response_schema.model_validate(obj, from_attributes=True).model_dump()
#                 )
#
#
# class UpdateMixin(BaseEndpointMixin):
#     """Добавляет PATCH /{id}"""
#     @classmethod
#     def register(cls):
#         @cls.router.patch("/{obj_id}")
#         async def update(obj_id: int, data: cls.update_schema, session: AsyncSession = Depends(get_session)):
#             try:
#                 await cls.service.update_obj(obj_id=obj_id, data_obj=data, session=session)
#             except DBError:
#                 cls.not_found(detail="Object not found")
#             else:
#                 return JSONResponse(
#                     status_code=HTTP_200_OK,
#                     content={"message": "Updated"}
#                 )
#
#
# class DeleteMixin(BaseEndpointMixin):
#     """Добавляет DELETE /{id}"""
#     @classmethod
#     def register(cls):
#         @cls.router.delete("/{obj_id}")
#         async def delete(obj_id: int, session: AsyncSession = Depends(get_session)):
#             try:
#                 await cls.service.delete_obj(obj_id=obj_id, session=session)
#             except DBError:
#                 cls.not_found(detail="Object not found")
#             else:
#                 return JSONResponse(
#                     status_code=HTTP_200_OK,
#                     content={"message": "Deleted"}
#                 )
#
#
# class RetrieveMixin(BaseEndpointMixin):
#     """Добавляет GET /{id}"""
#     @classmethod
#     def register(cls):
#         @cls.router.get("/{obj_id}")
#         async def get(obj_id: int, session: AsyncSession = Depends(get_session)):
#             obj = await cls.service.get_obj_by_id(obj_id=obj_id, session=session)
#             if not obj:
#                 cls.not_found(detail="Object not found")
#             return cls.response_schema.model_validate(obj, from_attributes=True)
#



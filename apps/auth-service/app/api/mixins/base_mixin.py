from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from starlette.status import HTTP_404_NOT_FOUND, HTTP_409_CONFLICT

from app.services import BaseService


class BaseEndpointMixin:
    router: APIRouter
    service: type[BaseService]
    response_schema: type[BaseModel] = None
    create_schema: type[BaseModel] = None
    update_schema: type[BaseModel] = None

    def __init__(self):
        """
        При создании экземпляра API вызываются все миксины,
        у которых определен __call__.
        """
        for base in type(self).__mro__:
            if base in (BaseEndpointMixin, object):
                continue
            call_method = getattr(base, "__call__", None)
            if callable(call_method) and base is not type(self):
                call_method(self)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.__name__.endswith("Mixin"):
            return

        if not getattr(cls, "router", None) or not isinstance(cls.router, APIRouter):
            raise ValueError(f"{cls.__name__}: требуется cls.router = APIRouter(...)")
        if not getattr(cls, "service", None):
            raise ValueError(f"{cls.__name__}: требуется cls.service = BaseService экземпляр")

    @staticmethod
    def not_found(detail="Object not found"):
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=detail)

    @staticmethod
    def conflict(detail="Conflict"):
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail=detail)
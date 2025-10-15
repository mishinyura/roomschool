from app.api.mixins.crud_mixin import CreateMixin, UpdateMixin, RetrieveMixin, DeleteMixin
from app.api.routers.addresses_api import address_api

__all__ = [
    "auth_router",
    "city_router",
    "address_api"
]
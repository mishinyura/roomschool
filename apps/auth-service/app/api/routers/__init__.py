from .addresses_api import address_api
from .auth_api import auth_router
from .cities_api import city_router

__all__ = [
    "auth_router",
    "city_router",
    "address_api"
]
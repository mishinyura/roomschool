from .addresses_api import address_api
from .auth_api import auth_router
from .cities_api import city_api
from .persons_api import person_api
from .roles_api import role_api
from .accounts_api import account_api

__all__ = [
    "auth_router",
    "city_api",
    "address_api",
    "person_api",
    "role_api",
    "account_api"
]
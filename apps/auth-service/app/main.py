import uvicorn

from fastapi import FastAPI

from app.api.routers import *
from app.core.config import settings
from app.core.db import create_tables
from app.middlewares import *

ROUTES = {
    '/auth': auth_router,
    '/cities': city_api.router,
    '/addresses': address_api.router,
    '/persons': person_api.router,
    '/roles': role_api.router,
    "/accounts": account_api.router
}

MIDDLEWARES = [
    error_handler_middleware,
    security_headers_middleware,
    request_timer_middleware,
]


def set_routes(app: FastAPI):
    for prefix, router in ROUTES.items():
        app.include_router(prefix=prefix, router=router)


def set_middlewares(app: FastAPI):
    for middleware in MIDDLEWARES:
        app.middleware("http")(middleware)


def main():
    app = FastAPI(
        debug=settings.app.debug,
        title='Auth Service',
        version=settings.app.app_version,
        description=settings.app.app_description,
        root_path=settings.app.app_mount
    )
    print(settings.app.debug, "OOO")

    set_middlewares(app)
    set_routes(app)

    @app.on_event("startup")
    async def startup_event():
        await create_tables()

    uvicorn.run(app, host=settings.app.app_host, port=settings.app.app_port)


if __name__ == '__main__':
    main()
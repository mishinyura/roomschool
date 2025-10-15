import uvicorn

from fastapi import FastAPI

from app.api.routers import *
from app.core.config import settings
from app.core.db import create_tables
from app.middlewares import *

ROUTES = {
    '/auth': auth_router,
    '/cities': city_router,
    '/addresses': address_api.router
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
    app = FastAPI(title='Auth Service')

    set_middlewares(app)
    set_routes(app)

    @app.on_event("startup")
    async def startup_event():
        await create_tables()

    uvicorn.run(app, host=settings.app.app_host, port=settings.app.app_port)


if __name__ == '__main__':
    main()
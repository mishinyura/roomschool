import uvicorn

from fastapi import FastAPI

from app.api import auth_router, city_router
from app.core.config import settings
from app.core.db import create_tables

ROUTES = {
    '/auth': auth_router,
    '/cities': city_router
}


def set_routes(app: FastAPI):
    for prefix, router in ROUTES.items():
        app.include_router(prefix=prefix, router=router)


def main():
    app = FastAPI(title='Auth Service')

    set_routes(app)

    @app.on_event("startup")
    async def startup_event():
        await create_tables()

    uvicorn.run(app, host=settings.app.app_host, port=settings.app.app_port)


if __name__ == '__main__':
    main()
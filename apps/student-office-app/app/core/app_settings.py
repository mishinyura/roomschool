from fastapi import FastAPI

from app.api import profile_router

ROUTES = {
    '/profile': profile_router
}


def set_routes(app: FastAPI):
    for prefix, router in ROUTES.items():
        app.include_router(prefix=prefix, router=router)


def get_app():
    app = FastAPI(title='student-office-app')
    set_routes(app)

    return app
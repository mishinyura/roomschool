import uvicorn
from fastapi import FastAPI

from app.api import callback_router, article_router, course_router
from app.core.db import create_tables

ROUTES = {
    "/callback": callback_router,
    "/articles": article_router,
    "/courses": course_router,
}


def main():
    app = FastAPI(title="Roomschool")

    for prefix, router in ROUTES.items():
        app.include_router(prefix=prefix, router=router)

    @app.on_event("startup")
    async def startup_event():
        await create_tables()

    uvicorn.run(app)


if __name__ == "__main__":
    main()

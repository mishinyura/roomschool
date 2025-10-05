from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app.core.db import get_session
from app.core.exceptions import PostNotFoundError
from app.services import article_services
from app.schemas.articles import ArticleInClient

article_router = APIRouter()


@article_router.get("/")
async def get_articles_list(session: AsyncSession = Depends(get_session)):
    posts = await article_services.get_all_posts(session)
    return posts


@article_router.post("/")
async def create_article(article_data: ArticleInClient, session: AsyncSession = Depends(get_session)):
    result = await article_services.add_new_article(article_data=article_data, session=session)
    return result


@article_router.get("/{slug}")
async def get_article(slug: str, session: AsyncSession = Depends(get_session)):
    try:
        post = await article_services.get_post_by_slug(slug=slug, session=session)
    except PostNotFoundError as ex:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=ex)
    else:
        return post

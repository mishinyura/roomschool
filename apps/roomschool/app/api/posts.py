from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app.core.db import get_session
from app.core.exceptions import PostNotFoundError
from app.services import posts_service

post_router = APIRouter()


@post_router.get("/")
async def get_posts_list(session: AsyncSession = Depends(get_session)):
    posts = await posts_service.get_all_posts(session)
    return posts


@post_router.post("/{post_id}")
async def get_post(post_id: int, session: AsyncSession = Depends(get_session)):
    return "OK"


@post_router.get("/{slug}")
async def get_post(slug: str, session: AsyncSession = Depends(get_session)):
    try:
        post = await posts_service.get_post_by_slug(slug=slug, session=session)
    except PostNotFoundError as ex:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=ex)
    else:
        return post

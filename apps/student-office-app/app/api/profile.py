from fastapi import APIRouter
from fastapi import Request

profile_router = APIRouter()


@profile_router.get('/')
async def my_profile():
    return {'profile': 'ok'}


@profile_router.post('/')
async def edit_profile(request: Request):
    data = await request.json()
    return data


@profile_router.patch('/')
async def update_profile():
    return 'update'
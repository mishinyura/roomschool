from fastapi import APIRouter

office_router = APIRouter()


@office_router.get('/profile')
async def my_profile():
    return {'profile': 'ok'}

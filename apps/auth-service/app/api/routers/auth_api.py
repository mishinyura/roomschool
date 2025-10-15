from fastapi import APIRouter

auth_router = APIRouter()


@auth_router.post('/')
def hello():
    return 'OK'
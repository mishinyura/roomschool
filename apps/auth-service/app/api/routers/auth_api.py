from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_200_OK

from app.services import auth_service
from app.core.security import get_current_user
from app.core.db import get_session
from app.core.exceptions import IncorrecPasswordError, AccountNotFoundError


class AuthAPI:
    router = APIRouter(tags=['Auth'])
    service = auth_service

    def __init__(self):
        self.router.add_api_route('/login', self.login, methods=['post'])

    async def login(
        self,
        form_data: OAuth2PasswordRequestForm = Depends(),
        session: AsyncSession = Depends(get_session),
    ):
        try:
            token = await self.service.authenticate(
                data=form_data,
                session=session
            )
        except IncorrecPasswordError as ex:
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail=str(ex))
        except AccountNotFoundError as ex:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=str(ex))
        else:
            return JSONResponse(status_code=HTTP_200_OK, content={"access_token": token, "token_type": "bearer"})



auth_api = AuthAPI()
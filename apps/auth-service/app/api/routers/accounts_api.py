from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_409_CONFLICT, HTTP_204_NO_CONTENT, HTTP_200_OK

from app.services import account_service
from app.schemas import AccountCreateSchema, AccountUpdateUsernameSchema, AccountUpdatePasswordSchema, AccountBaseSchema, AccountOutClientSchema, AccountFullOutClientSchema
from app.core.db import get_session

from app.api.mixins import CreateMixin, RetrieveMixin, DeleteMixin, UpdateMixin
from app.core.exceptions import DBError


class AccountAPI(DeleteMixin):
    router = APIRouter(tags=['Accounts'])
    service = account_service

    def __init__(self):
        super().__init__()

        self.router.add_api_route('/{uuid}', self.get_account, methods=['get'])
        self.router.add_api_route('/', self.create_user, methods=['post'])
        self.router.add_api_route('/password', self.update_password, methods=['patch'])

    async def get_account(self, uuid, session: AsyncSession = Depends(get_session)):
        try:
            account = await self.service.get_account_by_uuid(uuid=uuid, session=session)
        except DBError:
            raise HTTPException(status_code=404)
        else:
            return account

    async def create_user(
            self,
            data: AccountCreateSchema,
            session: AsyncSession = Depends(get_session)
    ):
        print("create_user вообще вызван")
        try:
            print("create_user вызван:", account_service)

            user = await self.service.create_new_account(data=data, session=session)
            print('UUU', user)
        except Exception as ex:
            HTTPException(HTTP_409_CONFLICT, detail="ERROR")
        else:
            return AccountBaseSchema.model_validate(user).model_dump(mode="json", by_alias=True)

    async def update_password(
            self,
            data: AccountUpdatePasswordSchema,
            session: AsyncSession = Depends(get_session)
    ):
        try:
            await self.service.update_password_by_uuid(data=data, session=session)
        except:
            HTTPException(HTTP_409_CONFLICT, detail="ERROR")
        else:
            return JSONResponse(status_code=HTTP_200_OK, content={"message": "Updated"})

    async def update_username(
            self,
            data: AccountUpdateUsernameSchema,
            session: AsyncSession = Depends(get_session)
    ):
        try:
            await self.service.update_password_by_uuid(data=data, session=session)
        except:
            HTTPException(HTTP_409_CONFLICT, detail="ERROR")
        else:
            return JSONResponse(status_code=HTTP_200_OK, content={"message": "Updated"})




account_api = AccountAPI()

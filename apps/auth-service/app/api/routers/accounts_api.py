from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_409_CONFLICT

from app.services import account_service
from app.schemas import AccountCreateSchema, AccountUpdateUsernameSchema, AccountUpdatePasswordSchema
from app.core.db import get_session

from app.api.mixins import CreateMixin, RetrieveMixin, DeleteMixin, UpdateMixin


class AccountAPI(DeleteMixin):
    router = APIRouter()
    service = account_service
    response_schema = AccountCreateSchema
    create_schema = AccountCreateSchema

    @router.post('/')
    async def create_user(
            self,
            data: AccountCreateSchema,
            session: AsyncSession = Depends(get_session)
    ):
        try:
            user = await self.service.create_new_account(data=data, session=session)
        except:
            HTTPException(HTTP_409_CONFLICT, detail="ERROR")

    @router.post('/password')
    async def update_password(
            self,
            data: AccountUpdatePasswordSchema,
            session: AsyncSession = Depends(get_session)
    ):
        try:
            result = await self.service.update_password_by_uuid(data=data, session=session)
        except:
            HTTPException(HTTP_409_CONFLICT, detail="ERROR")



account_api = AccountAPI()
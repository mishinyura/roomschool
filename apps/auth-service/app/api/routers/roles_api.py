from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_403_FORBIDDEN

from app.services import role_service
from app.schemas import RoleCreateSchema, RoleUpdateSchema, RoleOutClientSchema, RoleAccountCreateSchema

from app.api.mixins import CreateMixin, RetrieveMixin, DeleteMixin, UpdateMixin
from app.core.db import get_session


class RoleAPI(RetrieveMixin, CreateMixin, DeleteMixin, UpdateMixin):
    router = APIRouter(tags=['Roles'])
    service = role_service
    response_schema = RoleOutClientSchema
    create_schema = RoleCreateSchema
    update_schema = RoleUpdateSchema

    def __init__(self):
        super().__init__()
        self.router.add_api_route('/account', self.add_role_account, methods=['post'])
        self.router.add_api_route('/account', self.remove_role_account, methods=['delete'])

    async def add_role_account(self, data: RoleAccountCreateSchema, session: AsyncSession = Depends(get_session)):
        try:
            await self.service.add_new_role_on_account(relation=data, session=session)
        except:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN)
        else:
            return JSONResponse(status_code=HTTP_201_CREATED, content={'message': 'Created'})

    async def remove_role_account(self, role_data: RoleAccountCreateSchema, session: AsyncSession = Depends(get_session)):
        try:
            await self.service.remove_role_on_account(role_data=role_data, session=session)
        except:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN)
        else:
            return JSONResponse(status_code=HTTP_200_OK, content={'message': 'Deleted'})



role_api = RoleAPI()
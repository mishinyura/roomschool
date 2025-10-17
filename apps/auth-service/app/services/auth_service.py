import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import account_crud
from app.models import AccountModel
from app.services.base_service import BaseService
from app.services import account_service, role_service
from app.core.exceptions import IncorrecPasswordError, AccountNotFoundError
from app.core.security import create_access_token, verify_password, hash_password
from app.core.config import settings


class AuthService(BaseService):
    crud = account_crud
    model = AccountModel

    async def authenticate(self, data, session: AsyncSession):
        account = await account_service.get_account_by_username(data.username, session)
        role = await role_service.get_role_name_by_account(account_id=account.id, session=session)
        if not account:
            raise AccountNotFoundError
        elif not verify_password(data.password, account.hash_password):
            raise IncorrecPasswordError
        print(role, 'PPP')
        token_data = {
            "sub": str(account.uuid),
            "exp": settings.auth.access_token_expire_minutes,
            "role": role,
            "iat": datetime.datetime.now()
        }
        token = create_access_token(token_data)
        return token


auth_service = AuthService()
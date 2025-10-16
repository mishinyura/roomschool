from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import account_crud
from app.models import AccountModel
from app.services.base_service import BaseService
from app.services import account_service
from app.core.exceptions import IncorrecPasswordError, AccountNotFoundError
from app.core.security import create_access_token, verify_password


class AuthService(BaseService):
    crud = account_crud
    model = AccountModel


    async def authenticate(self, data, session: AsyncSession):
        account = await account_service.get_account_by_username(data.username, session)
        if not account:
            raise AccountNotFoundError
        elif not verify_password(data.password, account.hash_password):
            raise IncorrecPasswordError
        token_data = {
            "sub": str(account.uuid),
            "role": account.role if hasattr(account, "role") else "user"
        }
        token = create_access_token(token_data)
        return {"access_token": token, "token_type": "bearer"}


auth_service = AuthService()
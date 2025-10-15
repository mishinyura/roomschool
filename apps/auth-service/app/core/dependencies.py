from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.security import decode_access_token
from app.services import ac

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_access_token(token)
        user_id: int = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")

        user = await user_service.get_obj_by_id(user_id)
        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return user
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


def require_roles(*roles: str):
    """Проверка ролей через dependency injection"""
    async def wrapper(current_user=Depends(get_current_user)):
        if current_user.role.name not in roles:
            raise HTTPException(status_code=403, detail="Access denied")
        return current_user
    return wrapper

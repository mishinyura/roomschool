from fastapi import HTTPException, status, Request


class UserValidate:
    async def check_user_agent(self, user_agent: str):
        if not user_agent:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Missing User-Agent header"
            )

    async def check_api_key(self, key: str):
        if not key or key != "supersecretkey123":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid or missing API key"
            )

    async def validate(self, request: Request):
        await self.check_user_agent(request.headers.get("user-agent"))
        await self.check_api_key(request.headers.get("x-api-key"))


user_validate = UserValidate()
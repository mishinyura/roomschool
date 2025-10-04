from app.clients import admin_client
from app.core.exceptions import PhoneNotValidError
from app.core.validators import sanitize_text
from app.schemas import CallbackFormRequest


class CallbackService:
    def __init__(self):
        self.client = admin_client

    async def create_callback(self, **kwargs) -> bool:
        form_data = CallbackFormRequest(
            name=sanitize_text(kwargs.name).strip(),
            phone=sanitize_text(kwargs.phone).strip(),
            method=sanitize_text(kwargs.method).strip(),
        )
        print(form_data)
        if not form_data.phone.startswith("+7"):
            raise PhoneNotValidError()

        # response = await self.client.send_callback(request.dict())

        if True:
            return True
        return False


callback_service = CallbackService()

from fastapi import APIRouter, Form, HTTPException

from app.core.enums import MethodCommunicationTypes
from app.core.exceptions import PhoneNotValidError
from app.schemas import CallbackFormRequest
from app.services import callback_service

callback_router = APIRouter()


@callback_router.post("")
async def main_form_callback(
    name: str = Form(...),
    phone: str = Form(...),
    method: MethodCommunicationTypes = Form(...),
):

    try:
        if await callback_service.create_callback(form_data):
            return "OK"
        return "No OK"
    except PhoneNotValidError:
        raise HTTPException(status_code=400, detail="Phone not valid")

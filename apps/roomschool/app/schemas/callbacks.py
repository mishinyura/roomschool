from pydantic import BaseModel

from app.core.enums import MethodCommunicationTypes


class CallbackFormRequest(BaseModel):
    name: str
    phone: str
    method: MethodCommunicationTypes

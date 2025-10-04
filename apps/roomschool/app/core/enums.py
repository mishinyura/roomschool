from enum import Enum


class MethodCommunicationTypes(str, Enum):
    PHONE = "phone"
    TELEGRAM = "telegram"
    WHATSAPP = "whatsapp"
    EMAIL = "email"

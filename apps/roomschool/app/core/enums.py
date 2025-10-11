from enum import Enum


class MethodCommunicationTypes(str, Enum):
    PHONE = "phone"
    TELEGRAM = "telegram"
    WHATSAPP = "whatsapp"
    EMAIL = "email"

class UserRoleEnums(str, Enum):
    ADMIN = "admin"
    TEACHER = "teacher"
    PARENT = ""
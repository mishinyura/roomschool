from pydantic import BaseModel, EmailStr, constr
from datetime import date


class PersonCreateSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    gender: str
    birthday: date | None = None
    phone: constr(pattern=r'^\+?\d{10,15}$')
    email: EmailStr | None = None
    registration_address_id: int
    residential_address_id: int | None = None
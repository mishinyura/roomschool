from pydantic import BaseModel, EmailStr, constr
from datetime import date

from app.core.utils import make_partial_model


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


class PersonOutClientSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    gender: str
    birthday: date | None = None
    phone: constr(pattern=r'^\+?\d{10,15}$')
    email: EmailStr | None = None
    registration_address: str
    residential_address: str | None = None


PersonUpdateSchema = make_partial_model("PersonUpdateSchema", base_model=PersonCreateSchema)
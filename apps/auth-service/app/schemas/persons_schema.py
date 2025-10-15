from pydantic import BaseModel, EmailStr, constr, Field
from datetime import date

from app.core.utils import make_partial_model
from app.schemas.addresses_schema import AddressOutClientSchema


class PersonCreateSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    gender: str
    birthday: date | None = None
    phone: constr(pattern=r'^\+?\d{10,15}$')
    email: EmailStr | None = None
    registration_address_id: int | None = None
    residential_address_id: int | None = None


class PersonOutClientSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    gender: str
    birthday: date | None = None
    phone: constr(pattern=r'^\+?\d{10,15}$')
    email: EmailStr | None = None
    person_address_registration: AddressOutClientSchema = Field(None, alias="registration_address")
    person_address_living: AddressOutClientSchema | None = Field(None, alias="residential_address")

    class Config:
        populate_by_name = True


PersonUpdateSchema = make_partial_model("PersonUpdateSchema", base_model=PersonCreateSchema)
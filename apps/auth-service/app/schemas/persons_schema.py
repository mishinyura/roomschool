import uuid as py_uuid

from pydantic import BaseModel, EmailStr, constr, Field
from datetime import date, datetime

from app.core.utils import make_partial_model
from app.schemas.addresses_schema import AddressOutClientSchema
from app.core.enums import Gender


class PersonBaseSchema(BaseModel):
    uuid: py_uuid.UUID
    first_name: str
    last_name: str
    middle_name: str | None = None
    gender: Gender
    birthday: date | None = None
    phone: constr(pattern=r'^\+?\d{10,15}$')
    email: EmailStr | None = None
    registration_address_id: int | None = None
    residential_address_id: int | None = None
    created_at: datetime
    updated_at: datetime


class PersonCreateSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    gender: Gender
    birthday: date | None = None
    phone: constr(pattern=r'^\+?\d{10,15}$')
    email: EmailStr | None = None
    registration_address_id: int | None = None
    residential_address_id: int | None = None


PersonUpdateSchema = make_partial_model("PersonUpdateSchema", base_model=PersonCreateSchema)


class PersonOutClientSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    gender: Gender
    birthday: date | None = None
    phone: constr(pattern=r'^\+?\d{10,15}$')
    email: EmailStr | None = None
    person_address_registration: AddressOutClientSchema = Field(None, alias="registration_address")
    person_address_living: AddressOutClientSchema | None = Field(None, alias="residential_address")

    class Config:
        populate_by_name = True


class PersonPersonalDataSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    birthday: date | None = None


class PersonContactsSchema(BaseModel):
    phone: constr(pattern=r'^\+?\d{10,15}$')
    email: EmailStr | None = None
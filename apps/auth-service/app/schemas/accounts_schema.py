from datetime import datetime
import uuid as py_uuid

from pydantic import BaseModel, Field, field_validator, ConfigDict

from app.core.utils import make_partial_model
from app.schemas.persons_schema import PersonOutClientSchema


class AccountBaseSchema(BaseModel):
    id: int
    uuid: py_uuid.UUID
    person_id: int
    username: str
    hash_password: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class AccountCreateSchema(BaseModel):
    person_id: int
    username: str
    password: str


AccountUpdateSchema = make_partial_model("AccountUpdateSchema", AccountBaseSchema)


class AccountUpdatePasswordSchema(BaseModel):
    uuid: py_uuid.UUID
    old_password: str
    new_password: str


class AccountUpdateUsernameSchema(BaseModel):
    uuid: py_uuid.UUID
    username: str
    password: str

class AccountOutClientSchema(BaseModel):
    uuid: py_uuid.UUID
    username: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime


class AccountFullOutClientSchema(BaseModel):
    uuid: py_uuid.UUID
    username: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    person: PersonOutClientSchema


class AccountLoginSchema(BaseModel):
    uuid: py_uuid.UUID
    username: str
    hash_password: str
    is_active: bool
    is_verified: bool
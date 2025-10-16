from datetime import datetime
import uuid as py_uuid

from pydantic import BaseModel, Field, field_validator, ConfigDict

from app.core.utils import make_partial_model


class AccountBaseSchema(BaseModel):
    id: int
    person: int = Field(..., alias='person')
    username: str
    hash_password: str
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

from datetime import datetime

from pydantic import BaseModel, Field

from app.core.utils import make_partial_model


class AccountCreateSchema(BaseModel):
    person_id: int
    username: str
    password: str


class AccountBaseSchema(BaseModel):
    id: int
    person: int = Field(..., alias='person')
    username: str
    hash_password: str
    created_at: datetime
    updated_at: datetime


class AccountUpdatePasswordSchema(BaseModel):
    uuid:
    password: str


AccountUpdateSchema = make_partial_model("AccountUpdateSchema", Ac)
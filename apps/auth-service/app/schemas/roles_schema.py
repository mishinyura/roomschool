from pydantic import  BaseModel

from app.core.utils import make_partial_model
from app.core.enums import UserRole


class RoleBaseSchema(BaseModel):
    id: int
    name: UserRole
    description: str
    display: str


class RoleCreateSchema(BaseModel):
    name: UserRole
    description: str
    display: str


class RoleAccountCreateSchema(BaseModel):
    account_id: int
    role_id: int


class RoleOutClientSchema(BaseModel):
    description: str
    display: str


RoleUpdateSchema = make_partial_model("RoleUpdateSchema", RoleBaseSchema)
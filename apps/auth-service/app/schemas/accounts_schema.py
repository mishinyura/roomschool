from datetime import datetime

from pydantic import BaseModel


class AccountCreateSchema(BaseModel):
    person_id: int
    username: str
    password: str
    created_at: datetime
    updated_at: datetime
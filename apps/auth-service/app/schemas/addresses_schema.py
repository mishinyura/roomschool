from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional


class AddressBaseSchema(BaseModel):
    city_id: int = Field(..., description="ID города")
    street: str = Field(..., min_length=2, max_length=150)
    house_number: str = Field(..., min_length=1, max_length=10)
    flat_number: Optional[str] = Field(None, max_length=10)


class AddressUpdateSchema(BaseModel):
    street: Optional[str] = None
    house_number: Optional[str] = None
    flat_number: Optional[str] = None


class AddressOutClientSchema(BaseModel):
    city: str
    street: str
    house_number: str
    flat_number: str

    @field_validator("city", mode="before")
    def convert_city(cls, v):
        if hasattr(v, "name"):
            return v.name
        return v
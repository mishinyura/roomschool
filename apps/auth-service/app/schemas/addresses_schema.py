from pydantic import BaseModel


class AddressCreateSchema(BaseModel):
    street: str
    house_number: str
    flat_number: str
    city_id: int 
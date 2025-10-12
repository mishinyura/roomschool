from pydantic import BaseModel, constr


class CityCreateSchema(BaseModel):
    name: str
    time_zone: constr(pattern=r"^[A-Za-z_]+/[A-Za-z_]+$")

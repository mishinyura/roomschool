from pydantic import BaseModel, Field, constr, ConfigDict

from app.core.utils import make_partial_model


class CityCreateSchema(BaseModel):
    name: str
    time_zone: constr(pattern=r"^[A-Za-z_]+/[A-Za-z_]+$") = Field(
        ...,
        example="Europe/Moscow",
        description="Часовой пояс в формате Region/City"
    )


class CityBaseSchema(BaseModel):
    id: int
    name: str
    time_zone: constr(pattern=r"^[A-Za-z_]+/[A-Za-z_]+$") = Field(
        ...,
        example="Europe/Moscow",
        description="Часовой пояс в формате Region/City"
    )

    model_config = ConfigDict(extra="forbid")


CityUpdateSchema = make_partial_model("CityUpdateSchema", CityBaseSchema)
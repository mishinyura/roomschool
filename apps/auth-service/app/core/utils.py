from typing import Optional
from pydantic import BaseModel, Field, create_model, ConfigDict


def make_partial_model(name: str, base_model: type[BaseModel]) -> type[BaseModel]:
    fields = {}

    for field_name, field_info in base_model.model_fields.items():
        annotation = Optional[field_info.annotation]
        new_field = Field(
            default=None,
            description=field_info.description,
            examples=field_info.examples,
            title=field_info.title,
        )
        fields[field_name] = (annotation, new_field)

    return create_model(name, __base__=BaseModel, __config__=ConfigDict(extra="forbid"), **fields)
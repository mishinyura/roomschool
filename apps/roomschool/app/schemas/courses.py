from typing import Any

from pydantic import BaseModel, model_validator


class CourseBaseSchema(BaseModel):
    id: int
    slug: str
    title: str
    short_description: str | None
    main_description: str
    full_description: str
    price: int
    discount: int
    image: str | None
    is_archived: bool


class CourseOutClientSchema(BaseModel):
    title: str
    short_description: str | None
    main_description: str
    full_description: str
    price: int
    discount: int
    image: str | None


class CourseInClientSchema(BaseModel):
    slug: str | None
    title: str
    short_description: str | None
    main_description: str
    full_description: str
    price: int
    discount: int
    image: str | None
    is_archived: bool


class CourseUpdateSchema(BaseModel):
    id: int
    fields: dict[str, object]

    @model_validator(mode='after')
    def validate_fields(self):
        allowed = {"title", "short_description", "main_description", "full_description", "price", "discount", "image", "is_archived"}
        for key in self.fields.keys():
            if key not in allowed:
                raise ValueError(f"Поле '{key}' не разрешено для обновления")
        return self

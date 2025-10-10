from pydantic import BaseModel


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
    slug: str
    title: str
    short_description: str | None
    main_description: str
    full_description: str
    price: int
    discount: int
    image: str | None
    is_archived: bool
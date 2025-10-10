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


class CourseOutClient(BaseModel):
    title: str
    short_description: str | None
    main_description: str
    full_description: str
    price: int
    discount: int
    image: str | None


class CourseInClient(BaseModel):
    slug: str
    title: str
    short_description: str | None
    main_description: str
    full_description: str
    price: int
    discount: int
    image: str | None
    is_archived: bool
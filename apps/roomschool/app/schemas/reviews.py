from pydantic import BaseModel


class ReviewBaseSchema(BaseModel):
    id: int
    rating: int
    course_id: int | None
    description: str
    author: str
    link: str
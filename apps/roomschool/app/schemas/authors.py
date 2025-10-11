from pydantic import BaseModel


class AuthorInClient(BaseModel):
    name: str
    post: str
    image_url: str


class AuthorBase(BaseModel):
    id: int
    name: str
    post: str
    image_url: str

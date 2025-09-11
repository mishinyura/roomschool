from pydantic import BaseModel


class ProfileInfoSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    age: int
    coins: float
    awards: list
    hobby: str
    dream: str
    image_url: str


class UpdateProfileSchema(BaseModel):
    hobby: str
    dream: str



from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class BaseModel:
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

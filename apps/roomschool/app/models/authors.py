from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base, BaseModel


class AuthorModel(BaseModel, Base):
    __tablename__ = "authors"

    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=False)
    post: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, unique=False
    )
    image_url: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, unique=True
    )

    posts = relationship("PostsModel", back_populates="author")

from sqlalchemy import Boolean, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, BaseModel


class ArticleModel(BaseModel, Base):
    __tablename__ = "articles"

    slug: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, unique=False)
    author_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("authors.id"), nullable=False, unique=False
    )
    is_archived: Mapped[bool] = mapped_column(
        Boolean, nullable=False, unique=False, default=False
    )

    author = relationship("AuthorModel", back_populates="article")

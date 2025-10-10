from typing import Optional

from sqlalchemy import String, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, BaseModel


class ReviewModel(BaseModel, Base):
    __tablename__ = 'reviews'

    rating: Mapped[int] = mapped_column(Integer, nullable=False, unique=False)
    course_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("courses.id"), nullable=True, unique=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, unique=False)
    author: Mapped[str] = mapped_column(String(50), nullable=True, unique=False)
    link: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)

    course = relationship('CourseModel', back_populates='review')
from typing import Optional

from sqlalchemy import String, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, BaseModel


class CourseModel(BaseModel, Base):
    __tablename__ = 'courses'

    slug: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    short_description: Mapped[Optional[str]] = mapped_column(String(100), nullable=True, unique=False)
    main_description: Mapped[str] = mapped_column(String(255), nullable=False, unique=False)
    full_description: Mapped[str] = mapped_column(Text, nullable=False, unique=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False, unique=False)
    discount: Mapped[int] = mapped_column(Integer, nullable=False, unique=False, default=0)
    image: Mapped[Optional[str]] = mapped_column(String(255), nullable=True, unique=False, default=None)
    is_archived: Mapped[bool] = mapped_column(Boolean, nullable=False, unique=False, default=False)

    review = relationship('ReviewModel', back_populates='course')


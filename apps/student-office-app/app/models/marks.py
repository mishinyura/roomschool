from sqlalchemy import Integer, SmallInteger, DateTime, Text, ForeignKey, CheckConstraint, Enum as AlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, BaseModel
from app.core.enums import PeriodEnum


class Marks(BaseModel, Base):
    student_id: Mapped[int] = mapped_column(Integer, nullable=False)
    subject_id: Mapped[int] = mapped_column(Integer, nullable=False)
    grade_id: Mapped[int] = mapped_column(Integer, nullable=False)
    period: Mapped[PeriodEnum] = mapped_column(AlchemyEnum(PeriodEnum), nullable=False)
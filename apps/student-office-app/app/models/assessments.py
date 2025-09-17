import datetime

from sqlalchemy import Integer, SmallInteger, DateTime, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, BaseModel
from app.core.utils import moscow_now


class Assessments(BaseModel, Base):
    topic_id: Mapped[int] = mapped_column(ForeignKey('topics.topic_id'), nullable=False)
    grade_id: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    __table_args__ = (
        CheckConstraint('total_score BETWEEN 0 AND 10', name='check_score_range'),
    )

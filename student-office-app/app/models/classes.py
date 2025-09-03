from sqlalchemy import SmallInteger, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from base import Base, BaseModel


class Class(BaseModel, Base):
     : Mapped[int] = mapped_column(SmallInteger, nullable=False, unique=False)
    year: Mapped[int] - mapped_column(SmallInteger, nullable=False, unique=False)

    __table_args__ = (CheckConstraint(
        'number BETWEEN 1 AND 12', name='check_class_number_range'
    ))

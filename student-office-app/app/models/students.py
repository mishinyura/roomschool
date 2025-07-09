import uuid as py_uuid
from sqlalchemy import String, Integer, text, ForeignKey, Enum as AlchemyEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, BaseModel
from app.core.enums import StudentStatus


class Student(BaseModel, Base):
    uuid: Mapped[py_uuid.UUID] = mapped_column(
        UUID(as_uuid=True), server_default=text("gen_random_uuid()"), unique=True, index=True, nullable=False
    )
    code: Mapped[int] = mapped_column(Integer, unique=True, nullable=True)
    person_id: Mapped[int] = mapped_column(ForeignKey('persons.person_id'), nullable=False)
    account_id: Mapped[int] = mapped_column(ForeignKey('accounts.account_id'), nullable=False)
    status: Mapped[StudentStatus] = mapped_column(AlchemyEnum(StudentStatus), nullable=False, default=StudentStatus.AWAITING)
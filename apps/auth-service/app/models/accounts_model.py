import datetime
import uuid as py_uuid

from sqlalchemy import Integer, String, DateTime, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel, Base


class AccountModel(BaseModel, Base):
    __tablename__ = 'accounts'

    uuid: Mapped[py_uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        unique=True,
        server_default=text("gen_random_uuid()"),
        index=True,
        nullable=False
    )
    person_id: Mapped[int] = mapped_column(Integer, ForeignKey('persons.id'), unique=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    hash_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now())

    account_person = relationship("PersonModel", back_populates="person_account", lazy="selectin")
    account_role = relationship("AccountRoleModel", back_populates="account_role_account", lazy="selectin")

    def __repr__(self):
        string = f"<Account: username={self.username}>"
        return string
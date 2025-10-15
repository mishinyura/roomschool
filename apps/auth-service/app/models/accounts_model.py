import datetime

from sqlalchemy import Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel, Base


class AccountModel(BaseModel, Base):
    __tablename__ = 'accounts'

    person_id: Mapped[int] = mapped_column(Integer, ForeignKey('persons.id'), unique=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    hash_password: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now())

    account_person = relationship("PersonModel", back_populates="person_account", lazy="selectin")
    account_role = relationship("AccountRoleModel", back_populates="account_role_account", lazy="selectin")
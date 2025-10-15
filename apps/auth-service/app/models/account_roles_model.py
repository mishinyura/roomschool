from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class AccountRoleModel(Base):
    __tablename__ = "account_roles"

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id", ondelete="CASCADE"))
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"))

    account_role_account = relationship(
        "AccountModel",
        back_populates="account_role",
        foreign_keys=[account_id],
        lazy="selectin"
    )
    account_role_role = relationship(
        "RoleModel",
        back_populates="role_account",
        foreign_keys=[role_id],
        lazy="selectin"
    )
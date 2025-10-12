from sqlalchemy import String, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.models.base_model import Base, BaseModel


class RoleModel(BaseModel, Base):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, unique=False, nullable=True)

    role_account = relationship("AccountRoleModel", back_populates="account_role_role", cascade="all, delete-orphan")
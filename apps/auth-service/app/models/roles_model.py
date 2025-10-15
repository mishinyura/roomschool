from sqlalchemy import String, Text, Enum as OrmEnum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.models.base_model import Base, BaseModel

from app.core.enums import UserRole


class RoleModel(BaseModel, Base):
    __tablename__ = "roles"

    name: Mapped[UserRole] = mapped_column(OrmEnum(UserRole), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, unique=False, nullable=True)
    display: Mapped[str] = mapped_column(String, unique=False, nullable=True)

    role_account = relationship(
        "AccountRoleModel",
        back_populates="account_role_role",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
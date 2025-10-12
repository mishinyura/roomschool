from datetime import date, datetime

from sqlalchemy import String, Integer, Date, DateTime, Enum as AlchemyEnum, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import Base, BaseModel
from app.core.enums import Gender


class PersonModel(BaseModel, Base):
    __tablename__ = 'persons'

    first_name: Mapped[str] = mapped_column(String(150), nullable=False, unique=False)
    last_name: Mapped[str] = mapped_column(String(150), nullable=False, unique=False)
    middle_name: Mapped[str | None] = mapped_column(String(150), nullable=True, unique=False)
    gender: Mapped[Gender] = mapped_column(AlchemyEnum(Gender), nullable=False, unique=False)
    birthday: Mapped[date] = mapped_column(Date)
    phone: Mapped[str] = mapped_column(String(20), nullable=False, unique=False, index=True)
    email: Mapped[str | None] = mapped_column(String(250), nullable=True, unique=True, index=True)
    registration_address_id: Mapped[int] = mapped_column(Integer, ForeignKey("addresses.id"), nullable=False, unique=False)
    residential_address_id: Mapped[int] = mapped_column(Integer, ForeignKey("addresses.id"), nullable=True, unique=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now())

    person_address_registration = relationship("AddressModel", back_populates="address_person_registration", foreign_keys=[registration_address_id])
    person_address_living = relationship("AddressModel", back_populates="address_person_living", foreign_keys=[residential_address_id])
    person_account = relationship("AccountModel", back_populates="account_person")

    def __repr__(self) -> str:
        return f"<Person(id={self.id}, name={self.last_name} {self.first_name}, phone={self.phone})>"
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel, Base


class AddressModel(BaseModel, Base):
    __tablename__ = 'addresses'

    city_id: Mapped[int] = mapped_column(Integer, ForeignKey('cities.id'), nullable=False, unique=False)
    street: Mapped[str] = mapped_column(String(150), nullable=False, unique=False)
    house_number: Mapped[str] = mapped_column(String(10), nullable=False, unique=False)
    flat_number: Mapped[str | None] = mapped_column(String(10), nullable=True, unique=False)

    address_person_registration = relationship(
        "PersonModel",
        back_populates="person_address_registration",
        foreign_keys="PersonModel.registration_address_id"
    )
    address_person_living = relationship(
        "PersonModel",
        back_populates="person_address_living",
        foreign_keys="PersonModel.residential_address_id"
    )
    city = relationship("CityModel", back_populates="address")
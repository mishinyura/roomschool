from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import Base, BaseModel


class CityModel(BaseModel, Base):
    __tablename__ = 'cities'

    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    time_zone: Mapped[str] = mapped_column(String(50), nullable=False, unique=False)

    address = relationship("AddressModel", back_populates="city", lazy="selectin")

    def __repr__(self):
        return f"City(name={self.name}, tz={self.time_zone}"
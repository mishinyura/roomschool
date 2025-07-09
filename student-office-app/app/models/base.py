import inflect
from sqlalchemy import Column, Integer
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column

_inflector = inflect.engine()


class Base(DeclarativeBase):
    pass


class BaseModel:
    @declared_attr
    def __tablename__(self) -> str:
        return _inflector.plural(self.__name__.lower())

    @declared_attr
    def id(self):
        column_name = f"{self.__name__.lower()}_id"
        return Column(column_name, Integer, primary_key=True, index=True)
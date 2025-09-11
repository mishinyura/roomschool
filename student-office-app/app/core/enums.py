from enum import Enum


class StudentStatus(str, Enum):
    WAITING = "Поступает"
    STUDYING = "Учится"
    FINISHED = "Выпущен"
    EXPELLED = "Отчислен"


class PeriodEnum(str, Enum):
    QUARTER = 'Q'
    YEAR = 'Y'
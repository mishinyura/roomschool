from enum import Enum


class StudentStatus(str, Enum):
    AWAITING = "Поступает"
    STUDYING = "Учится"
    FINISHED = "Выпущен"
    EXPELLED = "Отчислен"
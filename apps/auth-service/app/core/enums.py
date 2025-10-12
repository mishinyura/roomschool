from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    TEACHER = "teacher"
    PARENT = "parent"
    STUDENT = "student"


class UserStatus(str, Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"
    ARCHIVED = "archived"


class Gender(str, Enum):
    MEN = "m"
    WOMEN = "w"
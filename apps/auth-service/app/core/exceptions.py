class DuplicateError(Exception):
    def __init__(self, message: str="Object already exists") -> None:
        self.message = message

    def __str__(self) -> str:
        return f"Duplicate Error: {self.message}"


class DBError(Exception):
    def __init__(self, message: str="Action failed") -> None:
        self.message = message

    def __str__(self) -> str:
        return f"Error: {self.message}"


class DBDuplicateError(Exception):
    def __init__(self, message: str="Object already exists") -> None:
        self.message = message

    def __str__(self) -> str:
        return f"DB Duplicate Error: {self.message}"
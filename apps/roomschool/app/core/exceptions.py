class PhoneNotValidError(Exception):
    def __init__(self):
        self.message = "The received phone number does not meet the requirements"

    def __str__(self):
        return f"Error: {self.message}"


class PostNotFoundError(Exception):
    def __init__(self):
        self.message = "Post not found"

    def __str__(self):
        return f"Error: {self.message}"


class ObjectNotFoundError(Exception):
    def __init__(self):
        self.message = "Not found"

    def __str__(self):
        return f"Error: {self.message}"


class SqlAlchemyError(Exception):
    def __init__(self):
        self.message = "It is impossible to add an element"

    def __str__(self):
        return f"Error: {self.message}"

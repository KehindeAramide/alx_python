"""Writing a class square that inherits from Rectangle(7-rectangle.py)."""
Rectangle = __import__('7-rectangle.py').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initializing a new square."""
        """
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

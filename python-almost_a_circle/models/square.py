"""Writting the class Square that inherits from Rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class inherits from Rectangle.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position (default is 0).
            y (int): The y-coordinate of the square's position (default is 0).
            id (int): The unique identifier of the square (default is None).
        """
        """Call the constructor of the Rectangle class and pass the necessary arguments"""
        super().__init__(size, size, x, y, id)

    """The __str__ method to return a string representation of the Square"""
    def __str__(self):
        """
        Return a string representation of the Square.

        Returns:
            str: A string in the format [Square] (<id>) <x>/<y> - <size>.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

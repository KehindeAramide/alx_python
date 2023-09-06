"""Creating the first Rectangle by that inherits from Base"""

from models.base import Base  
"""Import the Base class from base.py"""

class Rectangle(Base):
    """
    Rectangle class inherits from Base.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the rectangle's position.
        __y (int): The y-coordinate of the rectangle's position.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Calling the constructor of the Base class and pass the id"""
        super().__init__(id)
        
        """Private instance attributes"""
        self.__width = 0
        self.__height = 0
        self.__x = ()
        self.__y = ()

        self.width = width
        self.height = height
        self.x = x
        self.y = y
    """Getter for width"""
    @property
    def width(self, width):
        return self.__width

    """Setter for width"""
    @width.setter
    def width(self, width):
        self.__width = self.validate_integer(width, "width")

    """Getter for height"""
    @property
    def height(self, height):
        return self.__height

    """Setter for height"""
    @height.setter
    def height(self, height):
        self.__height = self.validate_integer(height, "height")

    """Getter for x"""
    @property
    def x(self, x):
        return self.__x

    """Setter for x"""
    @x.setter
    def x(self, x):
        self.__x = self.validate_non_negative_integer(x, "x")

    """Getter for y"""
    @property
    def y(self, y):
        return self.__y

    """Setter for y"""
    @y.setter
    def y(self, y):
        self.__y = self.validate_non_negative_integer(y, "y")

    """Validation method for integer attributes"""
    def validate_integer(self, value, attribute_name):
        """
        Validate that the value is an integer and greater than zero.
        Args:
            value (int): The value to be validated.
            attribute_name (str): The name of the attribute being validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than zero.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")
        return value

    """Validation method for non-negative integer attributes"""
    def validate_non_negative_integer(self, value, attribute_name):
        """
        Validate that the value is an integer and greater than or equal to zero.
        Args:
            value (int): The value to be validated.
            attribute_name (str): The name of the attribute being validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")
    """Public method to calculate and return the area"""
    def area(self):
        """
        Calculate and return the area of the Rectangle.
        Returns:
            int: The area of the Rectangle.
        """
        return self.__width * self.__height
    """Public method to display the Rectangle"""
    def display(self):
        """
        Print the Rectangle instance with '#' characters.
        """
        for _ in range(self.__height):
            print("#" * self.__width)
            """Override the __str__ method"""
    def __str__(self):
        """
        Return a string representation of the Rectangle.
        Format: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        Returns:
            str: The string representation of the Rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
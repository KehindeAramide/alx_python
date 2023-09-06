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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """Getter for width"""
    @property
    def width(self):
        return self.__width

    """Setter for width"""
    @width.setter
    def width(self, value):
        self.__width = value

    """Getter for height"""
    @property
    def height(self):
        return self.__height

    """Setter for height"""
    @height.setter
    def height(self, value):
        self.__height = value

    """Getter for x"""
    @property
    def x(self):
        return self.__x

    """Setter for x"""
    @x.setter
    def x(self, value):
        self.__x = value

    """Getter for y"""
    @property
    def y(self):
        return self.__y

    """Setter for y"""
    @y.setter
    def y(self, value):
        self.__y = value

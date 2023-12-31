"""Defines a class Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('5-base_geometry').BaseGeometry
"""Importing from 5-base_geometry """


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle."""
        bg = BaseGeometry()
        """Creating an instance for BaseGeometry."""
        attributes_and_methods = dir(bg)
        """Getting attributes and methods of instance"""
        class_attributes_and_methods = dir(BaseGeometry)
        """
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        
        return string

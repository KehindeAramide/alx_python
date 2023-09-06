"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle."""
        BaseGeometry = Rectangle()
        attributes_and_methods = dir(Rectangle)
        """Getting attributes and methods of instance"""
        class_attributes_and_methods = dir(Rectangle)

        """
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        """creating a rectangle """
    
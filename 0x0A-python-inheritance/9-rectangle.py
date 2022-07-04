#!/usr/bin/python3
"""Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

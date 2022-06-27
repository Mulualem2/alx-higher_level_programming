#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """Class that defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation attributes"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """Property to retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter to set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Property to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Calculates the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the permiter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

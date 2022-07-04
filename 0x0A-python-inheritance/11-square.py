#!/usr/bin/python3
"""Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square data that inherits from Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.integer_validator(size, size)
        self.__size = size

    def area(self):
        """Method to calculate area of the square"""

        return self.__size * self.__size

    def __str__(self):
        """print square description"""

        return "[Square] {}/{}".format(self.__size, self.__size)

#!/usr/bin/python3
"""A simple Square class"""


class Square:
    """class Square that defines a square and compute area"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size is 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)

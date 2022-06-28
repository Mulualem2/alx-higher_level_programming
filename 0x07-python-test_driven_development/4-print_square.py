#!/usr/bin/python3
"""
Module that defines a function that print a square using #
size must be an integer
if size is less than 0, raise a ValueError
"""


def print_square(size):
    """
    size is the size length of the square.
    function that prints a square with the character #."""

    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("")

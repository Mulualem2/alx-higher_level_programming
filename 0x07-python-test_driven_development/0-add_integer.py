#!/usr/bin/python3
"""Module that defines a function add_integer that adds 2 integers.
Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise a TypeError exception.
Returns an integer: the addition of a and b."""


def add_integer(a, b=98):
    """b is always 98 unless specified otherwise
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b"""

    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b

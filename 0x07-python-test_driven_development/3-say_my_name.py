#!/usr/bin/python3
"""
Module that defines function that prints
My name is <first name> <last name>.
first_name and last_name must be strings
"""


def say_my_name(first_name, last_name=""):
    """
    first_name and last_name must be strings.
    function that prints My name is <first name> <last name>."""
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {0} {1}".format(first_name, last_name))

#!/usr/bin/python3
"""Function that inherits"""


def inherits_from(obj, a_class):
    """Function that inherits"""

    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return isinstance(obj, a_class)

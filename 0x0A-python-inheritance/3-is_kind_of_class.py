#!/usr/bin/python3
""""returns True if the object or false"""


def is_kind_of_class(obj, a_class):
    """Function to check if return true or false"""

    if isinstance(obj, a_class):
        return True
    else:
        return False

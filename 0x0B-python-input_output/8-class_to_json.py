#!/usr/bin/python3
"""return the dictionary"""


def class_to_json(obj):
    """Returns the dict descr for JSON"""

    return obj.__dict__

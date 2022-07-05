#!/usr/bin/python3
"""return a JSON object"""
import json


def from_json_string(my_str):
    """return a python object"""

    return json.loads(my_str)

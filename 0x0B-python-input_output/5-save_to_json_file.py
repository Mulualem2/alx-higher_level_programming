#!/usr/bin/python3
"""function that writes an object to a text"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON"""

    with open(filename, mode="w", encoding="utf-8") as saveFile:
        json.dump(my_obj, saveFile)

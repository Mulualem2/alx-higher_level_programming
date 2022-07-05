#!/usr/bin/python3
""""load from a json file"""
import json


def load_from_json_file(filename):
    """Returns created object from a JSON file"""

    with open(filename, mode="r", encoding="UTF-8") as readFile:
        return json.load(readFile)

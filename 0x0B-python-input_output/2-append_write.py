#!/usr/bin/python3
"""append a string at the end of a file"""


def append_write(filename="", text=""):
    """A function that appends a file"""

    with open(filename, mode="a", encoding="utf-8") as appendFile:
        return appendFile.write(text)

#!/usr/bin/python3
"""Function that read files on UTF-8"""


def read_file(filename=""):
    """Read the file on UTF-8"""

    with open(filename, mode='r', encoding='utf-8') as read_File:
        print(read_File.read(), end="")

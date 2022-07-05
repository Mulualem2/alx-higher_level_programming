#!/usr/bin/python3
"""Function that write a file on UTF-8"""


def write_file(filename="", text=""):
    """Function that writes a file on UTF-8"""

    with open(filename, mode='w', encoding='utf-8') as write_File:
        return write_File.write(text)

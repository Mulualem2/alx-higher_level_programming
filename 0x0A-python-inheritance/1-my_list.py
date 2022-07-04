#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))

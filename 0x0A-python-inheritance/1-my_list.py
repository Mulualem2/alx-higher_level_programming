#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """prints the list sorted"""

    def print_sorted(self):
        """print the list sorted"""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))

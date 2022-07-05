#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """Contain student data"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return a dictionary"""

        return self.__dict__

#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """Contain student data"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return a dictionary"""

        if attrs is None or type(attrs) is not list:
                return self.__dict__
        else:
            temp_list = {}
            for element in attrs:
                if type(element) is not str:
                    return self.__dict__
                if element in self.__dict__.keys():
                    temp_list[element] = self.__dict__[element]
            return temp_list

    def reload_from_json(self, json):
        """Replace all items on json"""

        for items in json.keys():
            self.__dict__[items] = json[items]

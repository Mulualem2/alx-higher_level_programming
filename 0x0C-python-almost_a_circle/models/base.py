#!/usr/bin/python3
"""class base"""
import json
import os


class Base:
    """Base class of the other shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string repr to file"""
        new_list = []
        filename = cls.__name__ + '.json'
        if list_objs is not None:
            for i in range(len(list_objs)):
                new_list.append(list_objs[i].to_dictionary())
        jstring = cls.to_json_string(new_list)
        with open(filename, 'w') as my_file:
            my_file.write(jstring)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 2)
        elif cls.__name__ == 'Square':
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return list of instances"""
        filename = cls.__name__ + '.json'
        my_list = []
        if os.path.isfile(filename):
            with open(filename, 'r') as my_file:
                File = my_file.read()
                new_list = cls.from_json_string(File)
                for i in new_list:
                    my_list.append(cls.create(**i))
            return my_list
        else:
            return []

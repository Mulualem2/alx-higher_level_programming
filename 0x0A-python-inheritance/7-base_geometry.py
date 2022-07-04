#!/usr/bin/python3
"""
function to create basegeometry
"""


class BaseGeometry:
    """Empty class"""

    def area(self):
        """Function not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

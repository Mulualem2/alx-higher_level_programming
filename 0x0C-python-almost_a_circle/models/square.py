#!/usr/bin/python3
"""Class that builds a Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Build a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of Square"""
        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """Override str function to return message"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.__x,
                                                 self.__y,
                                                 self.__width)

    @property
    def size(self):
        """return size"""
        return self.__width

    @size.setter
    def size(self, size):
        """checks the size"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = size

    # Getter and checks the x
    @property
    def x(self):
        """return x"""
        return self.__x

    @x.setter
    def x(self, x):
        """checks the x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    # Getter and checks the y
    @property
    def y(self):
        """return y"""
        return self.__y

    @y.setter
    def y(self, y):
        """checks the y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def update(self, *args, **kwargs):
        """That assigns an argument to each attribute"""
        names = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, names[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in names:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dict representation of a Square"""
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['size'] = self.__width
        dictionary['x'] = self.__x
        dictionary['y'] = self.__y
        return dictionary

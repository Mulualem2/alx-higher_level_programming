#!/usr/bin/python3
"""Class that creates the Rectangle File"""
from models.base import Base


class Rectangle(Base):
    """Build a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle Class constructor"""
        # Call the super class with id
        super().__init__(id)

        # Width:
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        # Height:
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        # X:
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        # Y:
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    # Return and Checks the width
    @property
    def width(self):
        """Return the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Checks the width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    # Return and Checks the height
    @property
    def height(self):
        """Return the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Checks the height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    # Return and Checks the x
    @property
    def x(self):
        """Return the x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Checks the x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    # Return and Checks the y
    @property
    def y(self):
        """Return the y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Checks the y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """Calculates shape area"""
        return self.__width * self.__height

    def display(self):
        """Print the shape with character '#'"""
        for a in range(0, self.__y):
            print("")
        for i in range(0, self.__height):
            for b in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Override str function to return message"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """That assigns an argument to each attribute"""
        names = ["id", "width", "height", "x", "y"]
        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, names[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in names:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dict representation of a Rectangle"""

        dictionary = {}
        dictionary['id'] = self.id
        dictionary['width'] = self.__width
        dictionary['height'] = self.__height
        dictionary['x'] = self.__x
        dictionary['y'] = self.__y
        return dictionary

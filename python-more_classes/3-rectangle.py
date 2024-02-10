#!/usr/bin/python3
""" Class Rectangle that defines a rectangle """


class Rectangle:
    """ Define a rectangle with width and height """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """ height property and setter """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ width property and setter """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ Method to return rectangle area """
    def area(self):
        return self.height * self.width

    """ Method to return rectangle perimeter """
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    """ Return representation of the rectangle """
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for index in range(self.height):
            rectangle += "#" * self.width
            if index != self.height - 1:
                rectangle += "\n"
        return rectangle

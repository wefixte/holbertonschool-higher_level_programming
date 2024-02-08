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
        return self.height

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
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

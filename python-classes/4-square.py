#!/usr/bin/python3
""" Class that defines a square """


class Square:
    """ Define a square with its size """
    def __init__(self, size=0):
        self.__size = size

    """ Property to retrieve size """
    @property
    def size(self):
        return self.__size

    """ Property to set the value size """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        # Store the value passed to the setter and updated size value

    """ Return the current square area """
    def area(self):
        return self.__size * self.__size

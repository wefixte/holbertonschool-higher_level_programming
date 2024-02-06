#!/usr/bin/python3
""" Class that defines a square """


class Square:
    """ Define a square with its size """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    """ Return the current square area """
    def area(self):
        return self.__size * self.__size

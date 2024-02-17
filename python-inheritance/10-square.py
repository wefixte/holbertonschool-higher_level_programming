#!/usr/bin/python3
"""
Class Rectangle that inherits from BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle """

    def __init__(self, size):
        """ Init a square
        Args:
            size: int, side size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Return the area of a square
        Return:
            square area (int)
        """
        return self.__size ** 2

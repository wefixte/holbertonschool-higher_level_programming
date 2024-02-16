#!/usr/bin/python3
"""
Class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Define a rectangle """

    def __init__(self, width, height):
        """ Init a rectangle
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ Returns string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

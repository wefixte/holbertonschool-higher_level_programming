#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry():
    """ Represent class BaseGeometry """

    def area(self):
        """ No implementation """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate parameter as a positive int
        Args:
            name: string, name of the parameter
            value: int, parameter to validate
        Raises:
            TypeError: if value not an int
            ValueError: if value negative
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

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
        self.__height = height
        self.__width = width

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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3
"""

Function that adds 2 integers.

"""


def add_integer(a, b=98):
    """
    Args:
        a: First value.
        b: Second value. Defaults to 98.
    Raises:
        TypeError: If a or b is not an int or float.
    Returns:
        The addition of a and b.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b

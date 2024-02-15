#!/usr/bin/python3
"""
Define lookup function
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    Args :
        obj: object to loop up
    Return:
        list of available attributes and methods
    """
    return dir(obj)

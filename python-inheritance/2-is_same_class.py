#!/usr/bin/python3
"""
Define function returns T/F depend if object is an instance of class
"""


def is_same_class(obj, a_class):
    """ Function that return True or False if obj is an instance of a_class
    Args:
        obj: object
        a_class: class
    Return:
        True or False
    """
    return type(obj) is a_class

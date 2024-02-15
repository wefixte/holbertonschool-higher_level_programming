#!/usr/bin/python3
"""
Verified if object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """ Fonction that verified if object is an instance of a class
    Args:
        obj: object
        a_class: class
    Return:
        True or False
    """
    return isinstance(obj, a_class)

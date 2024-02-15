#!/usr/bin/python3
"""
Check if object is an instance of a class that inherited from specified class
"""


def inherits_from(obj, a_class):
    """ Fonction that verified if object is an instance
    of a class that inherited from the class
    Args:
        obj: object
        a_class: class
    Return:
        True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

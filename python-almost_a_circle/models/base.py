#!/usr/bin/python3
"""
Class Base for all other classes : manage id attribute
"""


class Base:
    """ class Base to manage id attribute in all sub-classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init and assign id it's value """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

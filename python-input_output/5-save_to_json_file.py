#!/usr/bin/python3
""" Function that writes object to text file, using a JSON representation """

import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file, using a JSON rep """

    with open(filename, 'w') as file:
        json.dump(my_obj, file)

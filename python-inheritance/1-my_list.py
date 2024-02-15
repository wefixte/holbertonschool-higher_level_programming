#!/usr/bin/python3
"""
Define inherits class MyList
"""


class MyList(list):
    """
    Add sorted printing
    """
    def print_sorted(self):
        """ Print list sorted in ascending sort"""
        sorted_list = sorted(self)
        print(sorted_list)

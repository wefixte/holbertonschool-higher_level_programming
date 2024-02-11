#!/usr/bin/python3
"""

Module to find the max integer in a list

"""


def max_integer(list=[]):
    """
    Function to find and return the max integer in a list of integers
    If the list is empty, the function returns None
    """
    # Check if list is valid
    if len(list) == 0:
        return None

    result = list[0]
    i = 1

    # Loop into list elements to find biggest integer
    while i < len(list):
        if list[i] > result:
            # Store max integer into result
            result = list[i]
        i += 1

    return result

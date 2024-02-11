#!/usr/bin/python3

""" Square-printing function """


def print_square(size):
    """
    Square-printing function
    Prints a square with the character #
    Args:
        size (int): size of square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """

    # Check if arguments are corrects
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print square
    for i in range(size):
        print("#" * size)

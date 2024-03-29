#!/usr/bin/python3
""" Class that defines a square """


class Square:
    """ Define a square with its size """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    """ Property to set the value size """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        # Store the value passed to the setter and updated size value

    @property
    def position(self):
        return self.__position

    """ Property to check position type """
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 \
             or not all(isinstance(num, int) for num in value) \
             or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """ Return the current square area """
    def area(self):
        return self.size * self.size

    """ Print the square with character : # """
    def my_print(self):
        if self.size == 0:
            print()
        else:
            # Blank lines to adjust vertical position
            for index in range(self.position[1]):
                print()
            # Print each row, " " to adjust horizontal position
            for index2 in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

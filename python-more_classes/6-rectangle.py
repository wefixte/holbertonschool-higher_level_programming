#!/usr/bin/python3
""" Class Rectangle that defines a rectangle """


class Rectangle:
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Init rectangle

         Args:
          width: rectangle width
          height: rectangle height
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    # height property and setter
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """height setter.

        Args:
            value (int): height value.
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # width property and setter
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """width setter.

        Args:
            value (int): width value.
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ Method to return rectangle area """
        return self.height * self.width

    def perimeter(self):
        """ Method to return rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """ Return representation of the rectangle """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for index in range(self.height):
            rectangle += "#" * self.width
            if index != self.height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """ Method to return string representation of rectangle """
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """ Method to print when rectangle is deleted """
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

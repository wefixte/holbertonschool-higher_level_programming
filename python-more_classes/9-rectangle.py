#!/usr/bin/python3

""" Class Rectangle that defines a rectangle """


class Rectangle:
    """ Empty rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Init rectangle

         Args:
          width: rectangle width
          height: rectangle height
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
            rectangle += str(self.print_symbol) * self.width
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

    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area
        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        Raises:
            TypeError: if either rectangles is not an instance of Rectangle
        Returns:
            Bigger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Return a new rectangle with width and height equal to size
        
        Args:
            size (int): size of the new rectangle
        
        Returns:
            cls: rectangle with same width and height
        """
        return cls(size, size)

#!/usr/bin/python3
"""
    This module defines a "Square" class.
    The Square class contains the methods
    for instantiating a square object of a
    certain size.
    The Square raises exceptions when bad
    values are entered.
    The Square has an area property implementation
"""


class Square:
    """
        Square class contains the __init__
        method that instantiates a square object
        If a bad value is passed, it raises an
        appropriate exception.
        Square class also contains the area method
        that returns the area of the square
    """
    def __init__(self, size=0):
        """
            This is the initializing method for the
            Square class
            Args:
                size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
            This is the method for calculating the area
            of a Square object instance of the Square class
            Args:
                self (object): This instance of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
            This is the method that prints a Square object instance
            of the Square class in # per unit size of the square
            Args:
                self (object): This instance of the square
        """
        if (self.__size == 0):
            print('\n', end="")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print('\n', end="")

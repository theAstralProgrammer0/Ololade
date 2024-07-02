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
    def __init__(self, size=0, position=(0, 0)):
        """
            This is the initializing method for the
            Square class
            Args:
                size (int): The size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")
            for i in range(0, self.__size):
                if self.__position[0] > 0:
                    print(" " * self.__position[0], end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print('\n', end="")

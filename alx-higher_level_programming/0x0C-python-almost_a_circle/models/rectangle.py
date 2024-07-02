#!/usr/bin/python3
"""This module contains the class that describes a rectangle"""
from models.base import Base


class Rectangle(Base):
    """This is the 'Rectangle' class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """This method initializes a rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """This method returns the area of a rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """This method displays the rectangle object as a grid of # symbols"""
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            for _ in range(self.__width):
                print("#", end="")
            print("\n", end="")

    def __str__(self):
        """This is the str magic method for 'print' statements to work with"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """This method updates the instance attributes of a rectangle object"""
        attr_list = ["id", "width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                if i > 4:
                    break
                setattr(self, str(attr_list[i]), arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """This method generates a dict based on the attribute-values of a
           rectangle instance
        """
        rect_dict = dict(x=self.x,
                         y=self.y,
                         id=self.id,
                         height=self.height,
                         width=self.width)
        return rect_dict

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is int:
            self.__width = width
        else:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is int:
            self.__height = height
        else:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is int:
            self.__x = x
        else:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is int:
            self.__y = y
        else:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

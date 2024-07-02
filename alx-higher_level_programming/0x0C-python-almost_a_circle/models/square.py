#!/usr/bin/python3
"""This is the module that contains the 'Square' class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the 'Square' class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This is the str magic method for 'print' statements to work with"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """This method updates the instance attributes of a square object"""
        attr_list = ["id", "size", "x", "y"]
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for i, arg in enumerate(args):
                if i > 3:
                    break
                setattr(self, str(attr_list[i]), arg)

    def to_dictionary(self):
        """This method generates a dict based on the attribute-values of a
           rectangle instance
        """
        sqr_dict = dict(id=self.id, x=self.x, size=self.width, y=self.y)
        return sqr_dict

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        if type(size) is int:
            self.width = size
            self.height = size
        else:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")

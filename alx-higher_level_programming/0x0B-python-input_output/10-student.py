#!/usr/bin/python3
"""This module contains a Student class"""


class Student:
    __slot__ = []
    """This is a Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This is a function that retrieves the json (dict) form of an obj"""
        i_dct = self.__dict__
        if attrs is None:
            return i_dct
        return {key: value for key, value in i_dct.items() if key in attrs}

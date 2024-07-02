#!/usr/bin/python3
"""
    Documentation needs to be fucking loooooooong
"""
import math


class MagicClass:
    """
        Magic Class Doc is the wayyyy bitch get used it it
    """
    def __init__(self, radius=0):
        """
            Initializing the radius to private value
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Area positive vibes only bruh"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Circumference Sir CUM ference. WTF????????"""
        return ((2 * math.pi) * self.__radius)

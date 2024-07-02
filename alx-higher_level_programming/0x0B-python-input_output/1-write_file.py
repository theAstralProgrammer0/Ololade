#!/usr/bin/python3
"""This module contains a function that writes a string to a text file (UTF8)
   and returns the number of characters written
"""


def write_file(filename="", text=""):
    """This function writes a string to a text file (UTF8)
       and returns the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)

#!/usr/bin/python3
"""This module reads the content of a file named @filename"""


def read_file(filename=""):
    """This function perfroms the module's function"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")

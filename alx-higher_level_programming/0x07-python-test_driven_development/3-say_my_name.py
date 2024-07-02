#!/usr/bin/python3
"""
say_my_name module:
This module provides a function to print a greeting message with the provided
names.
"""


def say_my_name(first_name, last_name=""):
    """
    Print a greeting message with the provided names.

    Args:
        first_name: The first name (required string).
        last_name: The last name (optional string, defaults to "").

    Raises:
        TypeError: If either name is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")

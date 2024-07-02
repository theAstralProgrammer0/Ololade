#!/usr/bin/python3
"""
add_integer module:
This module provides a function to add two integers together.
"""


def add_integer(a, b=98):
    """
    Adds two integers together, ensuring integer types and handling potential
    errors.

    Args:
        a: The first numner (required).
        b: The second number (optional, defaults to 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """
    if (not isinstance(a, int)) and (not isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, int)) and (not isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

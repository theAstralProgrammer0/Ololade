#!/usr/bin/python3
"""
print_square module:
This module provides a function to print a square of a specified size.
"""


def print_square(size):
    """
    Prints a square of size * size using '#' characters.

    Args:
        size: The size of the square (must be a non-negative integer).

    Raises:
        ValueError: If `size` is not an integer or is less than 0.

    Returns:
        None: This function does not return any value, it only prints the
        square.
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n") * size, end="")

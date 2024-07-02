#!/usr/bin/python3
"""
matrix_divided module:
This module provides a function to divide each element of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by a number, ensuring numerical types
    and handling potential errors.

    Args:
        matrix: A list of lists representing a matrix.
        div: The number to divide by.

    Returns:
        A new matrix with each element divided by div.

    Raises:
        TypeError: If the matrix is not a list of lists, or if its elements are
        not numbers.
        ZeroDivisionError: If div is zero.
    """
    if not (type(div) is int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (matrix == [] or (not isinstance(matrix, list)) or
            (not all(isinstance(row, list) for row in matrix)) or
            (not all(isinstance(num, int) or isinstance(num, float)
                     for row in matrix for num in row))):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    result = [[float(f"{num / div:.2f}") for num in row] for row in matrix]
    return result

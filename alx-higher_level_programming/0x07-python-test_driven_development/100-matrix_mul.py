#!/usr/bin/python3
"""
matrix_mul module:
This module provides a function to multiply two matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the resulting matrix.

    Args:
        m_a: The first matrix (list of lists of numbers).
        m_b: The second matrix (list of lists of numbers).

    Returns:
        List[List[float]]: The resulting matrix after multiplication.

    Raises:
        TypeError: If either matrix is not a list of lists of numbers,
        or if they have incompatible dimensions.
        ValueError: If either matrix is empty.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or all(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or all(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    if not all((isinstance(num, int) or isinstance(num, float)) for row in m_a
               for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(num, int) or isinstance(num, float)) for row in m_b
               for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(0, len(m_a)):
        temp = []
        for j in range(0, len(m_b[0])):
            summ = 0
            for k in range(0, len(m_a[0])):
                summ += m_a[i][k] * m_b[k][j]
            temp.append(summ)
        result.append(temp)
    return result

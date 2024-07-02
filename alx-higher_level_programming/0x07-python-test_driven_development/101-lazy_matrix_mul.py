#!/usr/bin/python3
"""
lazy_matrix_mul module:
This module provides a function to perform lazy matrix multiplication using
NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Performs lazy matrix multiplication using NumPy.

    Args:
        m_a: The first matrix (list of lists of numbers).
        m_b: The second matrix (list of lists of numbers).

    Returns:
        A NumPy array representing the matrix multiplication result. The actual
        calculation is deferred until elements are accessed.

    Raises:
        TypeError: If either matrix is not a list of lists of numbers, or if
        they have incompatible dimensions.
        ValueError: If either matrix is empty.
    """
    return np.matmul(m_a, m_b)

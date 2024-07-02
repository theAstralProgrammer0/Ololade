#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for col in row:
            new_row.append(col**2)
        new_matrix.append(new_row)
    return new_matrix

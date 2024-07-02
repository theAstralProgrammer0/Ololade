#!/usr/bin/python3
def square_matrix_map(my_list=[]):
    return list(map(lambda row: list(map(lambda x: x**2, row)), my_list))

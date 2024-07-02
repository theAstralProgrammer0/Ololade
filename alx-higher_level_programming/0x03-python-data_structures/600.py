#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix or not matrix[0]:
        print("{}".format('\n'), end="")
    else:
        for row in matrix:
            for i, num in enumerate(row):
                if i < len(row) - 1:
                    print("{:d} ".format(num), end="")
                else:
                    print("{:d}".format(num), end="")
            print("{}".format('\n'), end="")


#!/usr/bin/python3
def no_c(my_string):
    trans_table = {ord('c'): None, ord('C'): None}
    return my_string.translate(trans_table)

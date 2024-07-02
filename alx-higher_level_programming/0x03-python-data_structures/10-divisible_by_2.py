#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = my_list.copy()
    for idx, num in enumerate(bool_list):
        if num % 2 == 0:
            bool_list[idx] = True
        else:
            bool_list[idx] = False
    return bool_list

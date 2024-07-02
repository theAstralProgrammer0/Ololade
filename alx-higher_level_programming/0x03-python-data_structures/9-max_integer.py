#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maxim = my_list[0]
    for num in my_list:
        if maxim < num:
            maxim = num
    return maxim

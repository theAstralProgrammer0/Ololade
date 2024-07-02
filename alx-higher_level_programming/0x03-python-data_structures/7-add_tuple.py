#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    result = ()
    t_a = tuple_a
    t_b = tuple_b
    if len_a < 2:
        diff = 2 - len_a
        t_a = tuple_a + (0,) * diff
    if len_b < 2:
        diff = 2 - len_b
        t_b = tuple_b + (0,) * diff

    for i in range(2):
        result += tuple([t_a[i] + t_b[i]])
    return result

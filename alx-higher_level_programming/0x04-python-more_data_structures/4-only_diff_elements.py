#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set_1 = set_1 - set_1.intersection(set_2)
    new_set_2 = set_2 - set_2.intersection(set_1)
    return new_set_1.union(new_set_2)

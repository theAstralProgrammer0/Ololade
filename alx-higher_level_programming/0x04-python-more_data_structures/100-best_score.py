#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    key_list = list(a_dictionary.keys())
    best_key = key_list[0]
    for key_idx in range(len(key_list)):
        curr_key = key_list[key_idx]
        if a_dictionary[curr_key] > a_dictionary[best_key]:
            best_key = curr_key
    return best_key

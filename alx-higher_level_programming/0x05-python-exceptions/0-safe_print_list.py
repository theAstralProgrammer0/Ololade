#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
        except IndexError:
            pass
        else:
            count += 1
            i += 1
    print('\n', end="")
    return (count)

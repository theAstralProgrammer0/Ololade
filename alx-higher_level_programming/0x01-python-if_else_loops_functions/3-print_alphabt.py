#!/usr/bin/python3
def print_alpha():
    for i in range(97, 123):
        if chr(i) != 'q' and chr(i) != 'e':
            print("{}".format(chr(i)), end="")


print_alpha()

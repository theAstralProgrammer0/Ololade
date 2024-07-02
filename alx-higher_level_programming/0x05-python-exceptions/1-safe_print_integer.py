#!/usr/bin/python3
def safe_print_integer(value):
    printed = True

    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return not printed
    else:
        return printed

#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    printed = True

    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as err_msg:
        print("Exception: {}".format(err_msg), file=sys.stderr)
        return not printed
    else:
        return printed

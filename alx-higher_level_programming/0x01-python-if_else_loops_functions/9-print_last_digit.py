#!/usr/bin/python3
def print_last_digit(number):
    last_digit = str(number)[len(str(number)) - 1]
    if last_digit.isdigit():
        print(f"{last_digit}", end="")
    else:
        sys.stderr("Not a digit")
    return (last_digit)

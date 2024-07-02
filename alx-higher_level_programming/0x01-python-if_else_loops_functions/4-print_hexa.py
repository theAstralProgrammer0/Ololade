#!/usr/bin/python3
def main():
    print_hex()


def print_hex():
    for i in range(0, 99):
        print("{} = {}".format(i, hex(i)))


main()

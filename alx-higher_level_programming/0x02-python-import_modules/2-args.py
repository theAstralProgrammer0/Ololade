#!/usr/bin/python3
import sys


def main():
    length = len(sys.argv)
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for idx in range(1, len(sys.argv)):
            print("{}: {}".format(idx, sys.argv[idx]))


if __name__ == "__main__":
    main()

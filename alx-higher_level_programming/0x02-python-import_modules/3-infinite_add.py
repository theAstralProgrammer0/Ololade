#!/usr/bin/python3
import sys


def main():
    length = len(sys.argv)
    sum = 0
    for idx in range(1, length):
        sum += int(sys.argv[idx])
    print("{}".format(sum))


if __name__ == "__main__":
    main()

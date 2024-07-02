#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, op, b = sys.argv[1:4]
    ops = {"+": add,
           "-": sub,
           "*": mul,
           "/": div
           }
    if op in ops:
        result = ops[sys.argv[2]](int(a), int(b))
        print(f"{a} {op} {b} = {result}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == "__main__":
    main()

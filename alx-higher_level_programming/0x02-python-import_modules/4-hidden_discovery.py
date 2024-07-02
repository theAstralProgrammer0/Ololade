#!/usr/bin/python3
import hidden_4


def main():
    names_list = dir(hidden_4)
    s_n = sorted(item for item in names_list if not item.startswith("__"))
    for name in s_n:
        print(name)


if __name__ == "__main__":
    main()

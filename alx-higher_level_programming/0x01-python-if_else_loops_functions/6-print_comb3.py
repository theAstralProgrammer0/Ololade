#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i == j:
            continue
        elif int(str(i) + str(j)) > int(str(j) + str(i)):
            continue
        elif i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}, ".format(i, j), end="")

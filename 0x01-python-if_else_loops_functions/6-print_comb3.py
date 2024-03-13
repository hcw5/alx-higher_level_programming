#!/usr/bin/python3
for dg1 in range(0, 10):
    for dg2 in range(dg1 + 1, 10):
        if dg1 == 8 and dg2 == 9:
            print("{}{}".format(dg1, dg2))
        else:
            print("{}{}".format(dg1, dg2), end=", ")

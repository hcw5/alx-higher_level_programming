#!/usr/bin/python3
def print_sorted_dictionary(a_dic):
    for b, s in sorted(a_dic.items()):
        print("{}: {}".format(b, s))

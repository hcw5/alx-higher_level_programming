#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for b, s in list(a_dictionary.items()):
        if s is value:
            a_dictionary.pop(b)
    return a_dictionary

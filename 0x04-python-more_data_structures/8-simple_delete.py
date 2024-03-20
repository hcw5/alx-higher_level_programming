#!/usr/bin/python3
def simple_delete(a_dic, key=""):
    if key in a_dic:
        del a_dic[key]
    return a_dic

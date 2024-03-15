#!/usr/bin/python3

if __name__ == "__main__":
    """Print nos of argv and the corresponding value of arguments"""
    import sys

    argv_no = len(sys.argv) - 1
    if argv_no == 0:
        print("0 arguments.")
    elif argv_no == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argv_no))
    for i in range(argv_no):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

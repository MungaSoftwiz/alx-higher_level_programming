#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    if argc == 0:
        print("{:d} arguments.".format(0))
    if argc == 1:
        print("{} argument:".format(argc))
    elif argc > 0:
        print("{} arguments:".format(argc))
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))

#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    argc = len(sys.argv) - 1

    for arg in sys.argv[1:]:
        total += int(arg)
    if argc == 0:
        print("{}".format(0))
    elif argc > 0:
        print("{:d}".format(total))

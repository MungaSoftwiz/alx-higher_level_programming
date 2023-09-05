#!/usr/bin/python3
for ascii_value in range(97, 123):
    if ascii_value != 101 and ascii_value != 113:
        print("{:c}".format(ascii_value), end="")

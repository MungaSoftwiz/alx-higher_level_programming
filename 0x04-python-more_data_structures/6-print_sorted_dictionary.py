#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return None
    for key, value in sorted(a_dictionary.items()):
        print("{:s}: {}".format(key, value))

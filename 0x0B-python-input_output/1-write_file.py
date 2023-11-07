#!/usr/bin/python3
""" Module contains the function write_file """


def write_file(filename="", text=""):
    """ Function writes a string to a text file
    and returns the number of characters written
    """

    with open(filename, mode="w", encoding="UTF8") as f:
        return f.write(text)

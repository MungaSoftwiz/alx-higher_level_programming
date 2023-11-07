#!/usr/bin/python3
""" Module contains the append_write function """


def append_write(filename="", text=""):
    """ Function appends a string at the end of a text file
    and returns the number of characters added
    """

    with open(filename, mode="a", encoding="UTF8") as f:
        return f.write(text)

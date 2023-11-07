#!/usr/bin/python3
""" Module contains function read_file """


def read_file(filename=""):
    """ Function reads a text file and prints to stdout"""

    with open(filename, encoding="UTF8") as f:
        file_content = f.read()
    print(file_content, end="")

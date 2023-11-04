#!/usr/bin/python3
""" Module contains a function text_indentation() """


def text_indentation(text):
    """
    The function prints a text with 2 new lines after each
    special characters(.?:)

    Arguments:
        text (str): The string input parameter

    Raises:
        TypeError: Is raised if `text` is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    index = 0

    while index < len(text) and text[index] == ' ':
        index += 1

    while index < len(text):
        print(text[index], end="")
        if text[index] == "\n" or text[index] in characters:
            if text[index] in characters:
                print("\n")
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue
        index += 1

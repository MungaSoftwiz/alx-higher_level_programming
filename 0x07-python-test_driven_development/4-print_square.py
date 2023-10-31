#!/usr/bin/python3
""" Module prints a square """


def print_square(size):
    """
    Function takes in `size` and prints a square of `size`
    with the character '#'

    Arguments:
        size (int): The size of the square to be printed

    Raises:
        TypeError: If the size is not an integer
        ValueError: If size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be integer")

    for _ in range(size):
        print("#" * size)

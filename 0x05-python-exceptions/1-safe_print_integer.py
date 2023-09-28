#!/usr/bin/python3
def safe_print_integer(value):
    """Function prints an int in value"""

    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except ValueError:
        pass
    return False

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Function iterates over a list,
    prints elements and returns the count
    """

    try:
        count = 0
        for element in range(x):
            print(my_list[element], end="")
            count += 1
        print()
        return count
    except IndexError:
        pass
    print()
    return count

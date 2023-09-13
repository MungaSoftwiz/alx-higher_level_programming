#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0

    unique_set = set(my_list)
    for num in unique_set:
        total += num
    return total

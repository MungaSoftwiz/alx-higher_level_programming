#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    dup_str = ""
    for index in range(len(str)):
        if index != n:
            dup_str += str[index]
    return dup_str

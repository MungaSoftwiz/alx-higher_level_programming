#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for num in range(list_length):
        try:
            div_list = my_list_1[num] / my_list_2[num]
        except TypeError:
            print("wrong type")
            div_list = 0
        except ZeroDivisionError:
            print("division by 0")
            div_list = 0
        except IndexError:
            print("out of range")
            div_list = 0
        finally:
            result.append(div_list)
    return result

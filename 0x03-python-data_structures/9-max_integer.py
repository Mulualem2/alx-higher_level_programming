#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        my_list.sort()
        length = (len(my_list)) - 1
        return my_list[length]
    else:
        return

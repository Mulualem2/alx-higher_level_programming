#!/usr/bin/python3
def no_c(my_string):
    my_string_list = list(my_string)
    index = 0
    for i in my_string_list:
        if i == 'c' or i == 'C':
            my_string_list[index] = ""
        index += 1
    return "".join(my_string_list)

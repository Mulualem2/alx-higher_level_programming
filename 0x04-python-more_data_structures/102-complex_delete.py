#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy = a_dictionary.copy()
    for k, v in copy.items():
        if value in v:
            del a_dictionary[k]
    return a_dictionary

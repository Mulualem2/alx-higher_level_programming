#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = sorted(a_dictionary.keys())
    for i in new:
        print("{}: {}".format(i, a_dictionary[i]))

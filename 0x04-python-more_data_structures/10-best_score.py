#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        value = 0
        for i, j, in a_dictionary.items():
            if j > value:
                value = j
                name = i
        return name

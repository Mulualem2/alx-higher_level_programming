#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    avarage = 0
    tuplee = 1
    w = 0
    for j, v in enumerate(my_list):
        for i in range(len(v)):
            tuplee *= v[i]
        w += v[i]
        avarage += tuplee
        tuplee = 1
    avarage /= w
    return avarage

#!/usr/bin/python3
"""Program that finds the peaks in alist of unsorted integers"""


def find_peak(list_of_integers):
    '''
    Finds the peak integer
    '''
    list_length = len(list_of_integers)
    end = list_length - 1
    if not list_of_integers:
        return None
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[end] > list_of_integers[end - 1]:
        return list_of_integers[end]

    for nums in range(1, end):
        if list_of_integers[nums] > list_of_integers[nums + 1] and\
           list_of_integers[nums] > list_of_integers[nums - 1]:
            return list_of_integers[nums]
    return None

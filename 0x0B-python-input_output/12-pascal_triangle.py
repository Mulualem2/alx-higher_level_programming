#!/usr/bin/python3
"""Function that creates a pascal triangle"""


def pascal_triangle(n):
    """ends of each list in the matrix"""

    if n <= 0:
        return []

    res = []
    for element in range(n):
        if element is 0:
            res.append([1])
            continue
        if element is 1:
            res.append([1, 1])
            continue
        row = []
        for item in range(element + 1):
            row.append(item)
        for item in range(1, element):
            row[0] = 1
            row[element] = 1
            row[item] = res[element - 1][item] + res[element - 1][item - 1]
        res.append(row)

    return res

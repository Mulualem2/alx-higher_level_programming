#!/usr/bin/python3
"""Module that defines function that divides all elements of a matrix.
matrix must be a list of lists of integers or floats
All elements of the matrix should be divided by div
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix.
    Each row of the matrix must be of the same size
    div must be a number (integer or float)"""

    if type(matrix) is not list or matrix == [] or matrix is None:
        raise TypeError('matrix must be a matrix (list of lists)'
                        ' of integers/floats')
    if not all(isinstance(x, list) for x in matrix):
        raise TypeError('matrix must be a matrix (list of lists)'
                        ' of integers/floats')
    if not all(len(l) == len(matrix[0]) for l in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    for lists in matrix:
        if not all(isinstance(elems, (int, float)) for elems in lists):
            raise TypeError('matrix must be a matrix (list of lists)'
                            ' of integers/floats')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    newlist = [[round(elem / div, 2) for elem in lists] for lists in matrix]
    return newlist

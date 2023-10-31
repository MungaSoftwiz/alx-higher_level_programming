#!/usr/bin/python3
""" Module computes the division of a matrix """


def matrix_divided(matrix, div):
    """
    Function that divides all elements in a matrix by div

    Arguments:
        matrix (list, int, float): A list of lists
        div (int, float): The divisor to divide through the matrix

    Raises:
        TypeError: If matrix is not a list, integer or a number.
        If the div is not a float or an integer

    Return: The result of the divided list
    """
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(num / div, 2) for num in row] for row in matrix]

    return result

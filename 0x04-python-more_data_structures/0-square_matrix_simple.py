#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    new_matrix = [[col_num ** 2 for col_num in row] for row in matrix]
    return new_matrix

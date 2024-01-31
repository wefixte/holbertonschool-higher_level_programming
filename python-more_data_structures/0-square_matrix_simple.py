#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        square = []
        for col in row:
            square.append(col ** 2)
        result.append(square)
    return result

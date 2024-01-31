#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for index in range(len(matrix)):
        for index2 in range(len(matrix[index])):
            print(matrix [index][index2], end=" ")
        print()

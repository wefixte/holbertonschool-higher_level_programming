#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        index = 0
        for col in row:
            print("{:d}".format(col), end=" ")
            if index < len(row) - 1:
                print(" ", end="")
            index += 1
        print()

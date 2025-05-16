#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []  # Empty list to hold squared values
    for row in matrix:
        # Iterate through each row and square each element]
        squared_row = [x ** 2 for x in row]
        new_matrix.append(squared_row)
    return new_matrix

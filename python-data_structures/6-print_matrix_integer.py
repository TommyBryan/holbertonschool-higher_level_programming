#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in matrix:  # Iterate through each row in the matrix
        for i in range(len(row)):  # Iterate through each element in the row
            if i != len(row) - 1:  # Check if the element is not the last in the row
                # Print the element followed by a space (no newline)
                print("{:d}".format(row[i]), end=" ")
            else:
                # Print the last element in the row without a trailing space
                print("{:d}".format(row[i]), end="")
        # Print a newline after each row
        print()

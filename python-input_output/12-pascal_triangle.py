#!/usr/bin/python3
"""Module to generate Pascal's Triangle."""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal’s Triangle of size n.

    Args:
        n (int): Number of rows in Pascal’s Triangle.

    Returns:
        list: A list of lists of integers representing Pascal’s Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        previous_row = triangle[i - 1]
        new_row = [1]

        for j in range(len(previous_row) - 1):
            new_row.append(
                previous_row[j] + previous_row[j + 1]
            )

        new_row.append(1)
        triangle.append(new_row)

    return triangle

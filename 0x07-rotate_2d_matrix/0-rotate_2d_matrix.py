#!/usr/bin/python3
"""
rotating a 2D List or Matrix
"""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (_type_): A 2D matrix.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]

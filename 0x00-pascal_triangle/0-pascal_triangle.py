#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create def pascal_triangle(n):that returns list of list"""
    triangle = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            x = 1
            for j in range(1, i + 1):
                level.append(x)
                x = x * (i - j) // j
            triangle.append(level)
    return triangle

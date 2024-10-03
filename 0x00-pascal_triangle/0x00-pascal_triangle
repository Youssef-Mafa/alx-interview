#!/usr/bin/python3
"""Combined Pascal Triangle Module"""

def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's triangle of n"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        C = 1
        for j in range(i + 1):
            row.append(C)
            C = C * (i - j) // (j + 1)
        triangle.append(row)

    return triangle

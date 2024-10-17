#!/usr/bin/python3
"""Module for calculating the minimum number of operations to reach n H characters"""


def minOperations(n):
    """
    Determines the minimum number of operations required to result in exactly n 'H' characters.
    The operations are:
    - Copy All
    - Paste
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    # Check divisibility starting from 2 upwards
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

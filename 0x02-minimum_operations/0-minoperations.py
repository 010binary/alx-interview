#!/usr/bin/python3
"""
Module for 0-minoperations
"""

def minOperations(n: int) -> int:
    """
    getting the min operation
    to copy all and paste H
    """

    operations: int = 0
    divisor: int = 2

    if (n <= 1):
        return operations

    while (n > 1):
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations


#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n: int) -> int:
    """
    getting the min operation
    to copy all and paste H
    """
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations


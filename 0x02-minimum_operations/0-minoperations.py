#!/usr/bin/python3
"""
modula code
"""

def minOperations(n):
    num_ops = 0
    min_ops = 2
    while n > 1:
        while n % min_ops == 0:
            num_ops += min_ops
            n /= min_ops
        min_ops += 1
    return num_ops

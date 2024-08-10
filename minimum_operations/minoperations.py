#!/usr/bin/python3
"""execute only two operations in this file: Copy All and Paste.
Given a number n"""


def minOperations(n):
    """ Given a number n, calculates the fewest number of operations
    needed to result in exactly n H characters in the file"""
    if n < 2:
        return (0)
    res = 0
    for i in range(2, (n + 1)):
        while (n % i == 0):
            res += i
            n = n // i
    return (res)

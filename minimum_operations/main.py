#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 1000000
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 2000000
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 3000000
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

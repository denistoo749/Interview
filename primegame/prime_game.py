#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """ Return: name of the player that won the most rounds.
    If the winner cannot be determined, return None
    """
    if x < 1 or not nums:
        return None
    res = 0
    for i in range(x):
        res ^= nums[i % x]
    if res == 0:
        return "Maria"
    else:
        return "Ben"

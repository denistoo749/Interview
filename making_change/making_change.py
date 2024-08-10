#!/usr/bin/python3
"""Change comes from within"""
from collections import deque


def makeChange(coins, total):
    """ determine the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0
    queue = deque([(0, 0)])
    visited = [True] + [False] * total
    while queue:
        totalCoins, currentValue = queue.popleft()
        totalCoins += 1
        for coin in coins:
            nextValue = currentValue + coin
            if nextValue == total:
                return totalCoins
            if nextValue < total:
                if not visited[nextValue]:
                    visited[nextValue] = True
                    queue.append((totalCoins, nextValue))
    return -1

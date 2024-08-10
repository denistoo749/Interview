#!/usr/bin/python3
"""You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and each box
may contain keys to the other boxes"""


def join(l1, l2):
    """joins"""
    res = []
    for e in l2:
        res += l1[e]
    return (res)


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""
    index = 0
    total = list(set(boxes[0]) | {0})
    added = True
    while added:
        added = False
        for j in join(boxes, total[index:]):
            if j not in total:
                total.append(j)
                index += 1
                added = True
    return (len(total) == len(boxes))

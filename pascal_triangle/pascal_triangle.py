#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascal’s triangle of n"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    else:
        # recursive call
        res_arr = pascal_triangle(n - 1)
        # use previous row to calculate current row
        # every row starts with 1
        cur_row = [1]
        prev_row = res_arr[-1]
        for i in range(len(prev_row) - 1):
            # sum of 2 entries directly above
            cur_row.append(prev_row[i] + prev_row[i + 1])
        # every row ends with 1
        cur_row += [1]
        res_arr.append(cur_row)
        return (res_arr)

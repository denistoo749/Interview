#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    m = len(grid)
    n = len(grid[0])
    land = 0
    neighbour = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                land += 1
                if i < m-1 and grid[i+1][j] == 1:
                    neighbour += 1
                if j < n-1 and grid[i][j+1] == 1:
                    neighbour += 1
    return land * 4 - 2 * neighbour

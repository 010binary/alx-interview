#!/usr/bin/python3
"""
solving the perimeter thing
"""


def island_perimeter(grid):
    perimeter = 0

    rows=len(grid)
    cols=len(grid[0])

    for r in range(rows):
        for c in range(cols):
            # Check if the current cell is land
            if grid[r][c] == 1:
                # Check all four directions (up, down, left, right)

                # Check upward (if it's out of bounds or water)
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1

                # Check downward (if it's out of bounds or water)
                if r == rows-1 or grid[r+1][c] == 0:
                    perimeter += 1

                # Check leftward (if it's out of bounds or water)
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1

                # Check rightward (if it's out of bounds or water)
                if c == cols-1 or grid[r][c+1] == 0:
                    perimeter += 1

    return perimeter

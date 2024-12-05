#!/usr/bin/env python3

from os import path
import itertools

data = """
####...#
......#.
#..#.##.
.#...#.#
..###.#.
##.###..
.#...###
.##....#""".strip().split("\n")

testdata = """.#.
..#
###"""

def render(grid):
    for z in range(-1, 2):
        print("z:", z)
        for y in range(-1, 2):
            line = []
            for x in range(-1, 2):
                coordinate = (x, y, z)
                line.append("#" if coordinate in grid else ".")
            print("".join(line))

    print()

def solve(inp, dims):
    def neighbors(cord):
        count = 0
        for d in itertools.product(*((-1, 0, 1) for _ in range(dims))):
            ncord = tuple(c + dc for c, dc in zip(cord, d))
            if cord == ncord:
                continue
            if ncord in grid:
                count += 1
                if count > 3:
                    return count
        return count

    grid = set()
    mins = [-1 for _ in range(dims)]
    maxs = [1 for _ in range(dims)]

    for y, line in enumerate(inp.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                grid.add((x, y) + tuple(0 for _ in range(dims - 2)))

    maxs[0] = maxs[1] = y + 1

    for _ in range(6):
        new_grid = set()

        for cord in itertools.product(
            *(range(lo, hi + 1) for lo, hi in zip(mins, maxs))
        ):
            n = neighbors(cord)
            if cord in grid:
                if n in (2, 3):
                    new_grid.add(cord)
            elif n == 3:
                new_grid.add(cord)

        grid = new_grid
        mins = [m - 1 for m in mins]
        maxs = [m + 1 for m in maxs]

        render(grid)
        input("Next >")

    return len(grid)


print("Part 1:", solve(testdata, 3))
#print("Part 2:", solve(inp, 4))
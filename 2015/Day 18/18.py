"""
--- Day 18: Like a GIF For Your Yard ---
After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed.
You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights,
he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's
next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it
(including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always
count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light
marked B, which is on an edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.

The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
All of the lights update simultaneously; they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......
After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?

--- Part Two ---
You flip the instructions over; Santa goes on to point out that this is all just an implementation of
Conway's Game of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought:
four lights, one in each corner, are stuck on and can't be turned off. The example above will actually run like this:

Initial state:
##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:
#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:
#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:
#...##
####.#
..##.#
......
##....
####.#

After 4 steps:
#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:
##.###
.##..#
.##...
.##...
#.#...
##...#
After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state,
how many lights are on after 100 steps?
"""
import copy

inputdata = open("input.data").read().strip().splitlines()

WIDTH = len(inputdata)
NEIGHBORS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

def render(matrix):
    print()
    for row in matrix:
        print("".join(row))

def init():
    matrix = []
    for y in range(WIDTH):
        matrix.append(WIDTH * [0])
        for x in range(WIDTH):
            light = inputdata[y][x]
            matrix[y][x] = "#" if light == "#" else "."
    return matrix

def step(matrix):
    matrix_copy = copy.deepcopy(matrix)
    for y in range(WIDTH):
        for x in range(WIDTH):
            neighbors_on = neighbor_count((x, y), matrix)
            if matrix[y][x] == "#":
                matrix_copy[y][x] = "#" if neighbors_on in (2, 3) else "."
            else:
                if neighbors_on == 3:
                    matrix_copy[y][x] = "#"

    return copy.deepcopy(matrix_copy)

def neighbor_count(at, matrix) -> int:
    neighbors = 0
    for neighbor_pos in NEIGHBORS:
        check_pos = (at[0] + neighbor_pos[0], at[1] + neighbor_pos[1])
        if check_pos[0] < 0 or check_pos[0] >= WIDTH or check_pos[1] < 0 or check_pos[1] >= WIDTH:
            continue

        light = matrix[check_pos[1]][check_pos[0]]
        neighbors += 1 if light == "#" else 0

    return neighbors

def apply_error(matrix):
    matrix[0][0] = "#"
    matrix[0][WIDTH-1] = "#"
    matrix[WIDTH-1][0] = "#"
    matrix[WIDTH-1][WIDTH-1] = "#"

def count_lights(matrix) -> int:
    lights = 0
    for row in matrix:
        lights += len(list(filter(lambda x: x == "#", row)))
    return lights

def part1():
    matrix = init()

    for i in range(100):
        matrix = step(matrix)

    print("Part 1: %s lights are on" % count_lights(matrix))

def part2():
    matrix = init()
    apply_error(matrix)

    for i in range(100):
        matrix = step(matrix)
        apply_error(matrix)


    print("Part 2: %s lights are on" % count_lights(matrix))
#part1()
part2()
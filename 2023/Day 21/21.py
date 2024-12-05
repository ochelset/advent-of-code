import itertools
from collections import Counter

data = open("input.data").read().strip().split("\n")

test_data = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
""".strip().split("\n")

xdata = test_data

width = len(data[0])
height = len(data)
rocks = set()
steps = 0
possibilities = set()
new_positions = []

for y in range(height):
    for x in range(width):
        if data[y][x] == "#":
            rocks.add((x, y))
        if data[y][x] == "S":
            new_positions.append((x, y))

def render():
    for y in range(height):
        row = ''
        for x in range(width):
            if (x, y) in rocks:
                row += '#'
            elif (x, y) in new_positions:
                row += 'O'
            else:
                row += '.'
        print(row)

possibilities = 0
while steps < 64:
    #print("Step", steps+1, " - possible pos", len(new_positions), new_positions)
    posses = new_positions[::]
    new_positions = []
    while len(posses):
        pos = posses.pop(0)
        for next_pos in [(-1,0), (0,-1), (1,0), (0,1)]:
            np = (pos[0]+next_pos[0], pos[1]+next_pos[1])
            if np not in rocks and np not in new_positions:
                new_positions.append(np)
    possibilities = len(new_positions)

    #render()
    #input()
    steps += 1

print("Part 1:", possibilities)


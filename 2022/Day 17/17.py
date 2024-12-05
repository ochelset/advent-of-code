from itertools import cycle
from collections import deque

data = open("input.data").read().strip()
data = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
DIRS = {">": 1, "<": -1}

rocks = [
    [
        [1, 1, 1, 1],
    ],

    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],

    [
        [0, 0, 1],
        [0, 0, 1],
        [1, 1, 1]
    ],

    [
        [1],
        [1],
        [1],
        [1]
    ],

    [
        [1, 1],
        [1, 1]
    ]
]


def get_coverage(rock, pos):
    coverage = set()
    for y in range(len(rock) - 1, -1, -1):
        for x in range(len(rock[y])):
            if not rock[y][x]:
                continue
            coverage.add((x + pos[0], y + pos[1]))

    return coverage


def get_boundaries(rock, pos):
    edges = [0, 0, 0, pos[1]]

    for y in range(len(rock)):
        for x in range(len(rock[y])):
            if not rock[y][x]:
                continue

            if y + pos[1] > edges[1]:
                edges[1] = y + pos[1]
            if pos[1] - y > edges[3]:
                edges[3] = pos[1] - y

    return edges


def render(rock, pos, begin=0):
    coverage = get_coverage(rock, pos)
    for y in range(begin, 0, 1):
        row = "|"
        for x in range(7):
            if (x, y) in coverage:
                row += "@"
            elif (x, y) in chamber:
                row += "#"
            else:
                row += "."

        row += "|"
        print(row)
    print(9 * "-")


def move(pos=(0, 0), dir=(0, 1)) -> (int, int):
    return (pos[0] + dir[0], pos[1] + dir[1])


def rest(rock, pos):
    coverage = get_coverage(rock, pos)
    for tile in coverage:
        chamber[tile] = True


width = 7
chamber = {}

for x in range(7):
    chamber[(x, 0)] = True


def part1():
    global chamber

    fallen = 0
    j = 0
    top = 0

    while True:
        for i in range(len(rocks)):
            rock = rocks[i]
            fallen += 1
            left = 2
            height = len(rock)

            start = top - 3 - height
            pos = (left, start)

            while True:
                # push
                jet = data[j]
                j += 1
                if j >= len(data):
                    j = 0
                push = [(-1, 0), (1, 0)][jet == ">"]

                jet_pos = move(pos, push)
                coverage = get_coverage(rock, jet_pos)

                end = False
                for tile in coverage:
                    if tile in chamber:
                        end = True
                        break
                    if tile[0] < 0 or tile[0] >= 7:
                        end = True
                        break

                if not end:
                    pos = jet_pos

                # fall
                next_pos = move(pos)

                coverage = get_coverage(rock, next_pos)
                end = False
                for tile in coverage:
                    if tile in chamber:
                        end = True
                        break

                if end:
                    rest(rock, pos)
                    if pos[1] < top:
                        top = pos[1]
                        start = top - height
                    break

                pos = next_pos

            if fallen == 2022:
                return abs(top)


def part2():
    global chamber, rocks
    pattern = []

    fallen = 0
    j = 0
    top = 0

    while True:
        for i in range(len(rocks)):
            rock = rocks[i]
            fallen += 1
            left = 2
            height = len(rock)

            start = top - 3 - height
            pos = (left, start)

            while True:
                # render(rock, pos, start)
                # input()

                # push
                jet = data[j]
                j += 1
                if j >= len(data):
                    j = 0
                push = [(-1, 0), (1, 0)][jet == ">"]
                # print("jet push", jet, j, len(data))

                jet_pos = move(pos, push)
                coverage = get_coverage(rock, jet_pos)

                end = False
                for tile in coverage:
                    if tile in chamber:
                        end = True
                        break
                    if tile[0] < 0 or tile[0] >= 7:
                        end = True
                        break

                if not end:
                    pos = jet_pos

                # render(rock, pos, start)
                # input()

                # fall
                # print("fall")
                next_pos = move(pos)

                coverage = get_coverage(rock, next_pos)
                end = False
                for tile in coverage:
                    if tile in chamber:
                        end = True
                        break

                if end:
                    prev_top = top
                    rest(rock, pos)
                    drop = pos[1] - start

                    if pos[1] < top:
                        top = pos[1]
                        start = top - height

                    diff = prev_top - top
                    pattern.insert(0, drop)
                    middle = int(len(pattern) / 2)
                    a = pattern[:middle]
                    b = pattern[middle:]
                    # print("Inc", diff, len(a), len(b), "Drop", drop)
                    if len(a) == len(b) and len(a) > 2:  # and sum(a) == sum(b):
                        print("Check pattern")
                        print(a)
                        print(b)

                        input()

                    # input()
                    break

                pos = next_pos

            if fallen == 2022:
                print("XXX", abs(top))
                return abs(top)

            # if fallen == 1000000000000:
            #    print("Part 2:", abs(top))

            # if fallen % 20 == 0:
            #    print(fallen, abs(top))
            #    input()


# print("Part 1:", part1())
part2()

wind = cycle(enumerate(DIRS[x] for x in data))
print(data)
print(wind)
while True:
    x = next(wind)
    print(x)
    input()

from collections import deque

test = False
data = open("input.data").read().splitlines()
if test:
    data = """
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
""".strip().splitlines()

    datxa = """
.....
..##.
..#..
.....
..##.
.....
""".strip().splitlines()

scan = {}
DIRS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
WIDTH = len(data[0])
HEIGHT = len(data)
world = [0, 0, WIDTH, HEIGHT]

for y in range(HEIGHT):
    for x in range(WIDTH):
        char = data[y][x]
        if char != "#":
            continue
        scan[(x, y)] = 0


def adjacent(pos, start) -> tuple:
    north = [(0, -1, 'N', DIRS[0]), (1, -1, 'NE', DIRS[0]), (-1, -1, 'NW', DIRS[0])]
    south = [(0, 1, 'S', DIRS[1]), (1, 1, 'SE', DIRS[1]), (-1, 1, 'SW', DIRS[1])]
    west = [(-1, 0, 'W', DIRS[2]), (-1, -1, 'NW', DIRS[2]), (-1, 1, 'SW', DIRS[2])]
    east = [(1, 0, 'E', DIRS[3]), (1, -1, 'NE', DIRS[3]), (1, 1, 'SE', DIRS[3])]

    neighbors = deque(north + south + west + east)
    neighbors.rotate(-start * 3)
    empty = 0
    for i, neighbor in enumerate(neighbors):
        npos = (pos[0] + neighbor[0], pos[1] + neighbor[1])
        if npos not in scan:
            empty += 1
        else:
            empty = 0

        if empty == 3:
            return (pos[0] + neighbor[3][0], pos[1] + neighbor[3][1])

        if (i + 1) % 3 == 0:
            empty = 0


def is_alone(pos) -> bool:
    global scan

    for neighbor in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
        if (pos[0] + neighbor[0], pos[1] + neighbor[1]) in scan:
            return False

    return True


def render():
    global scan, world

    for y in range(world[1], world[3] + 1):
        row = ""
        for x in range(world[0], world[2]):
            if (x, y) in scan:
                row += "#"
            else:
                row += "."
        print(row)
    print()


render()

rounds = 0
while True:
    proposals = {}
    for elf in scan.keys():
        if is_alone(elf):
            continue

        proposal = adjacent(elf, rounds % 4)
        if proposal is None:
            continue

        proposal = (proposal[0], proposal[1])
        if proposal not in proposals:
            proposals[proposal] = []
        proposals[proposal].append(elf)

    moved = 0
    for proposal in proposals.keys():
        if len(proposals[proposal]) > 1:
            continue

        old_pos = proposals[proposal].pop()
        next_dir = scan[old_pos]
        del scan[old_pos]

        scan[proposal] = 0

        if proposal[0] < world[0]:
            world[0] = proposal[0] - 1
        if proposal[0] > world[2]:
            world[2] = proposal[0] + 1
        if proposal[1] < world[1]:
            world[1] = proposal[1] - 1
        if proposal[1] > world[3]:
            world[3] = proposal[1] + 1

        moved += 1

    rounds += 1

    world = [5, 0, 5, 0]
    for elf in scan.keys():
        if elf[0] < world[0]:
            world[0] = elf[0]
        if elf[0] > world[2]:
            world[2] = elf[0]
        if elf[1] < world[1]:
            world[1] = elf[1]
        if elf[1] > world[3]:
            world[3] = elf[1]

    if rounds == 10:
        render()
        empty = (abs(world[0] - world[2] - 1) * abs(world[1] - world[3] - 1)) - len(scan.keys())
        print("Part 1:", empty)

    if moved == 0:
        render()
        print("Part 2:", rounds)
        break

from collections import deque

test = True
data = open("input.data").read().splitlines()
SIZE = 50

if test:
    data = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.
    
10R5L5R10L4R5L5""".splitlines()
    SIZE = 4

path = data.pop()
data.pop()

world = {"frame": [0, 0, 0, 0]}
start = None
visited = {}
DIRS = deque([(1, 0, ">", 0), (0, 1, "v", 1), (-1, 0, "<", 2), (0, -1, "^", 3)])

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == " ":
            continue

        world[(x, y)] = char
        if start is None:
            start = (x, y)

        if x > world["frame"][2]:
            world["frame"][2] = x
        if y > world["frame"][3]:
            world["frame"][3] = y

current = start
direction = DIRS[0]


def render(cube=None):
    global world
    for y in range(world["frame"][3] + 1):
        row = ""
        for x in range(world["frame"][2] + 1):
            if (x, y) not in world:
                row += " "
                continue

            if (x, y) == current:
                row += DIRS[0][2]
                continue

            if (x, y) in visited:
                row += visited[(x, y)]
                continue

            if cube is not None and (x, y) in cube:
                if world[(x, y)] == "#":
                    row += "#"
                else:
                    row += str(cube[(x, y)])
                continue

            row += world[(x, y)]
        print(row)
    print()


def wrap(start, size, cube: dict):
    global world

    for x in range(start[0], start[0] + size):
        for y in range(start[1], start[1] + size):
            for z in range(start[2], start[2] + size):
                # pos = (coord[0] + x), coord[1] + (y * transform[1]), coord[2] + (z * transform[2]))
                cube[(x, y)] = start[2]
                # cube[pos] = start[3]


def fold(side_start, coord, transform, cube):
    corner = int(SIZE / 2)
    for x in range(-corner, corner):
        for y in range(-corner, corner):
            for z in range(-corner, corner):
                xx = [x, x + 1][x >= 0]
                yy = [y, y + 1][y >= 0]
                zz = [z, z + 1][z >= 0]

                wc = (side_start[0] + x + corner, side_start[1] + y + corner, side_start[2])
                sc = ((xx * transform[0]), (yy * transform[1]), (zz * transform[2]))
                if sc in cube:
                    continue

                cube[sc] = wc
                # pos = (coord[0] + (x * transform[0]), coord[1] + (y * transform[1]), coord[2] + (z * transform[2]))

                print(">", sc, wc)
                input()


def part1():
    global current, path, world

    while path != "":
        next_turn = len(path)
        l = r = 1000
        if "R" in path:
            r = path.index("R")
        if "L" in path:
            l = path.index("L")

        next_turn = min(l, r, next_turn)
        steps = int(path[:next_turn])
        turn = path[next_turn:next_turn + 1]

        for i in range(1, steps + 1):
            next_pos = (current[0] + DIRS[0][0], current[1] + DIRS[0][1])
            if next_pos not in world:
                while next_pos not in world:
                    next_pos = (next_pos[0] + DIRS[0][0], next_pos[1] + DIRS[0][1])
                    if next_pos[0] >= world["frame"][2]:
                        next_pos = (0, next_pos[1])
                    elif next_pos[0] < 0:
                        next_pos = (world["frame"][2], next_pos[1])
                    if next_pos[1] >= world["frame"][3]:
                        next_pos = (next_pos[0], 0)
                    elif next_pos[1] < 0:
                        next_pos = (next_pos[0], world["frame"][3])
            if world[next_pos] == "#":
                break

            visited[current] = DIRS[0][2]
            current = next_pos

        if turn == "R":
            DIRS.rotate(-1)
        elif turn == "L":
            DIRS.rotate(1)
        else:
            render()
            last = [1000 * (current[1] + 1), 4 * (current[0] + 1), DIRS[0][3]]
            print("Part 1:", last, sum(last))
            break

        path = path[next_turn + 1:]


def part2(cubed=False):
    global current, path, world

    cube = {}  # {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}}
    if cubed:
        if test:
            wrap((8, 0, 1), SIZE, cube)
            wrap((0, 4, 2), SIZE, cube)
            wrap((4, 4, 3), SIZE, cube)
            wrap((8, 4, 4), SIZE, cube)
            wrap((8, 8, 5), SIZE, cube)
            wrap((12, 8, 6), SIZE, cube)
        else:
            wrap((50, 0, 1), SIZE, cube)
            wrap((50, 50, 4), SIZE, cube)
            wrap((100, 0, 6), SIZE, cube)
            wrap((50, 100, 5), SIZE, cube)
            wrap((0, 100, 3), SIZE, cube)
            wrap((0, 150, 2), SIZE, cube)

        side_start = (8, 4, 4)
        transform = (1, 1, 0)
        # fold((8, 0, 1), (-2, -2, -2, 1), (1, 0, 1), cube)
        # fold((8, 4, 4), (-2, -2, -2, 4) (1, 1, 0), cube)

    render(cube)
    input()

    while path != "":
        next_turn = len(path)
        l = r = 1000
        if "R" in path:
            r = path.index("R")
        if "L" in path:
            l = path.index("L")

        next_turn = min(l, r, next_turn)
        steps = int(path[:next_turn])
        turn = path[next_turn:next_turn + 1]

        current_side = cube[current]
        heading = DIRS[0][2]

        for i in range(1, steps + 1):
            next_pos = (current[0] + DIRS[0][0], current[1] + DIRS[0][1])
            if next_pos not in world:
                render(cube)
                print("Wrap over from", current_side, current, ">", next_pos, DIRS[0][2])
                print(next_pos[0] % SIZE, next_pos[1] % SIZE)
                if test:
                    rotation = 0
                    if current_side == 4 and DIRS[0][2] == ">":
                        next_pos = (SIZE * 4 - (next_pos[1] % SIZE) - 1, SIZE * 2)
                        rotation = -1
                    if current_side == 5 and DIRS[0][2] == "v":
                        next_pos = (SIZE - (next_pos[0] % SIZE) - 1, SIZE * 2 - 1)
                        rotation = -2
                    if current_side == 3 and DIRS[0][2] == "^":
                        print("SNAP", next_pos[0] % SIZE)
                        next_pos = (SIZE * 2, next_pos[0] % SIZE)
                        rotation = -1

                    if world[next_pos] != "#":
                        DIRS.rotate(rotation)
                    else:
                        break

                    print("TO", next_pos, DIRS[0], world[next_pos])
                input()

            if world[next_pos] == "#":
                # print("WALL")
                break

            visited[current] = heading
            current = next_pos

            # render()
            # input()

        if turn == "R":
            DIRS.rotate(-1)
        elif turn == "L":
            DIRS.rotate(1)
        else:
            render()
            last = [1000 * (current[1] + 1), 4 * (current[0] + 1), DIRS[0][3]]
            print("Part 1:", last, sum(last))
            break

        path = path[next_turn + 1:]


part1()
part2(True)

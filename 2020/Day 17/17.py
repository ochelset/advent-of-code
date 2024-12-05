data = """
####...#
......#.
#..#.##.
.#...#.#
..###.#.
##.###..
.#...###
.##....#""".strip().split("\n")

testdata = """
.#.
..#
###""".strip().split("\n")

BOOT_SEQUENCE_LENGTH = 6
ACTIVE = True
INACTIVE = False

space = {}
cyclus = 1

def init(state: list):
    global space
    space = { "min": 0, "max": len(state)}

    for y, line in enumerate(state):
        for x, state in enumerate(line):
            #print("X;Y;Z", x,y,0, ACTIVE if state == "#" else INACTIVE)
            space[(x, y, 0)] = ACTIVE if state == "#" else INACTIVE

def render(z: int):
    global space
    xMin = space["min"]
    yMin = space["min"]
    xMax = space["max"]
    yMax = space["max"]

    print("z:", z, yMin, yMax)
    for y in range(yMin, yMax):
        line = []
        for x in range(xMin, xMax):
            coordinate = (x, y, z)
            line.append("#" if space.get(coordinate) else ".")
        print("".join(line))

    print()

def count_active_neighbors(coordinate: tuple, space: dict, cube: list) -> int:
    active = 0
    for neighbor in cube:
        neighbor_coordinate = []
        for i in range(len(coordinate)):
            neighbor_coordinate.append(coordinate[i] + neighbor[i])

        active += 1 if space.get(tuple(neighbor_coordinate)) else 0

    return active

def cycle(cube: list):
    global space
    global cyclus
    print("> cycle", cyclus)

    cyclus += 1
    space["min"] -= 2
    space["max"] += 2
    shadow_space = space.copy()

    for w in range(space["min"]-1, space["max"]+1):
        for z in range(space["min"]-1, space["max"]+1):
            for y in range (space["min"]-1, space["max"]+1):
                for x in range(space["min"]-1, space["max"]+1):
                    coordinate = (x, y, z, w)

                    active_neighbors = count_active_neighbors(coordinate, space, cube)
                    #input()

                    current_state = shadow_space.get(coordinate) or INACTIVE
                    new_state = current_state
                    if current_state == ACTIVE:
                        if active_neighbors in (2, 3):
                            new_state = ACTIVE
                        else:
                            new_state = INACTIVE
                    elif current_state == INACTIVE and active_neighbors == 3:
                            new_state = ACTIVE

                    shadow_space[coordinate] = new_state

    space = shadow_space.copy()

    result = 0
    for coordinate in space.keys():
        if coordinate in ["min", "max"]:
            continue
        result += 1 if space[coordinate] else 0

    print("Active", result)

def generate_cube(sides: int):
    cube = []
    for w in range(-1, 2):
        for z in range(-1, 2):
            for y in range(-1, 2):
                for x in range(-1, 2):
                    if x == 0 and y == 0 and z == 0 and w == 0:
                        continue

                    cube.append((x, y, z, w))

    return cube

def part1(data: list):
    init(data)

    cube = generate_cube(sides=4)

    # boot sequence
    for _ in range(BOOT_SEQUENCE_LENGTH):
        cycle(cube)

    result = 0
    for coordinate in space.keys():
        if coordinate in ["min", "max"]:
            continue
        result += 1 if space[coordinate] else 0

    print("Part 1:", result)

part1(testdata)
print(space)
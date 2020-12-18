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

ROUNDS = 6
ACTIVE = True
INACTIVE = False

CUBE = [
    (-1, 1, 1), (0, 1, 1), (1, 1, 1),
    (-1, 0, 1), (0, 0, 1), (1, 0, 1),
    (-1, -1, 1), (0, -1, 1), (1, -1, 1),

    (-1, 1, 0), (0, 1, 0), (1, 1, 0),
    (-1, 0, 0), (1, 0, 0),
    (-1, -1, 0), (0, -1, 0), (1, -1, 0),

    (-1, 1, -1), (0, 1, -1), (1, 1, -1),
    (-1, 0, -1), (0, 0, -1), (1, 0, -1),
    (-1, -1, -1), (0, -1, -1), (1, -1, -1)
]

space = {}

def init(state: list):
    global space
    space = {}

    for y, line in enumerate(state):
        for x, state in enumerate(line):
            space[(x, y, 0)] = ACTIVE if state == "#" else INACTIVE

def render(z: int):
    xMin = 0
    yMin = 0
    xMax = 3
    yMax = 3
    for y in range(yMin, yMax):
        line = []
        for x in range(xMin, xMax):
            coordinate = (x, y, z)
            line.append("#" if space.get(coordinate) else ".")
        print("".join(line))

    print()

def count_active_neighbors(coordinate: tuple, space: dict) -> int:
    active = 0
    for neighbor in CUBE:
        neighbor_coordinate = (coordinate[0] + neighbor[0], coordinate[1] + neighbor[1], coordinate[2] + neighbor[2])
        #print(neighbor_coordinate, space.get(neighbor_coordinate))
        active += 1 if space.get(neighbor_coordinate) else 0

    return active

def cycle():
    global space
    print("> cycle start")

    shadow_space = space.copy()

    for z in range(-2, 2):
        for y in range (-2, 2):
            for x in range(-2, 2):
                coordinate = (x, y, z)


                #for coordinate in space.keys():
                active_neighbors = count_active_neighbors(coordinate, shadow_space)

                current_state = shadow_space.get(coordinate) or INACTIVE
                new_state = current_state
                if current_state == ACTIVE:
                    if active_neighbors in (2, 3):
                        new_state = ACTIVE
                    else:
                        new_state = INACTIVE
                elif current_state == INACTIVE:
                    if active_neighbors == 3:
                        new_state = ACTIVE

                shadow_space[coordinate] = new_state
                print(coordinate, current_state, ">", new_state, active_neighbors)

        input()

    space = shadow_space.copy()

def part1(data: list):
    init(data)
    render(0)
    cycle()
    render(-1)
    render(0)
    render(1)

    result = 0
    for coordinate in space.keys():
        result += 1 if space[coordinate] else 0

    print("Part 1:", result)

part1(testdata)
print(space)
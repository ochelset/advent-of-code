from collections import deque

test = False
data = open("input.data").read().splitlines()

if test:
    data = """
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
""".strip().splitlines()

DIRS = [(0, -1, "^"), (1, 0, ">"), (0, 1, "v"), (-1, 0, "<")]
MOVES = [(1, 0), (0, 1), (0, -1), (-1, 0), (0, 0)]
WIDTH = len(data[0])
HEIGHT = len(data)

world = [0, 0, WIDTH, HEIGHT]
ground = {}
blizzards = {}
pos = (1, 0)
target = (0, 0)

for y in range(HEIGHT):
    for x in range(WIDTH):
        char = data[y][x]
        if char == "#":
            ground[(x, y)] = 1
            continue

        blizzard = "^>v<".find(char)
        if blizzard != -1:
            if (x, y) not in blizzards:
                blizzards[(x, y)] = []
            blizzards[(x, y)].append(DIRS[blizzard])

        if y == HEIGHT - 1 and char == ".":
            target = (x, y)


def move():
    global blizzards, ground, world

    new_blizzards = {}
    for blizzard in blizzards.keys():
        for movement in blizzards[blizzard]:
            updated = (blizzard[0] + movement[0], blizzard[1] + movement[1])
            if updated in ground:
                updated = (updated[0] - (movement[0] * (WIDTH - 2)), updated[1] - (movement[1] * (HEIGHT - 2)))

            if updated not in new_blizzards:
                new_blizzards[updated] = []
            new_blizzards[updated].append(movement)

    return new_blizzards


def render():
    global ground, world

    for y in range(world[1], world[3]):
        row = ""
        for x in range(world[0], world[2]):
            if (x, y) in blizzards:
                if len(blizzards[(x, y)]) == 1:
                    row += blizzards[(x, y)][0][2]
                else:
                    row += str(len(blizzards[(x, y)]))
                continue

            if (x, y) == pos:
                row += "E"
                continue

            if (x, y) in ground:
                row += "#"
            else:
                row += "."
        print(row)


rounds = 0
render()
print()

while True:
    rounds += 1
    blizzards = move()

    possibles = []
    for my_move in MOVES:
        updated = (pos[0] + my_move[0], pos[1] + my_move[1])
        if updated[0] > 0 and updated[1] >= 0 and updated not in ground and updated not in blizzards:
            possibles.append(updated)
    pos = possibles[0]
    print(possibles)

    print("Minute", rounds)
    render()

    if pos == target:
        print("Part 1:", rounds)
        break

    input()

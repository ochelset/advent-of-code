inputdata = open("input.data").read().strip().splitlines()

WIDTH = len(inputdata[0])
HEIGHT = len(inputdata)

seafloor = {}

def render():
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            if (x, y) in seafloor:
                row += seafloor[(x, y)]
            else:
                row += "."
        print(row)
    print()

def move() -> bool:
    global seafloor

    next_seafloor = {}
    moves = 0
    for step in [(1, 0, ">"), (0, 1, "v")]:
        for pos, cucumber in seafloor.items():
            if cucumber != step[2]:
                next_seafloor[pos] = cucumber
                continue

            new_pos = (pos[0]+step[0], pos[1]+step[1])
            if new_pos[0] >= WIDTH:
                new_pos = (0, new_pos[1])
            if new_pos[1] >= HEIGHT:
                new_pos = (new_pos[0], 0)

            if new_pos not in seafloor:
                moves += 1
                next_seafloor[new_pos] = cucumber
            else:
                next_seafloor[pos] = cucumber

        seafloor = next_seafloor.copy()
        next_seafloor = {}

    return moves > 0

for y in range(HEIGHT):
    for x in range(WIDTH):
        if inputdata[y][x] != ".":
            seafloor[(x, y)] = inputdata[y][x]

i = 0
while True:
    i += 1
    moved = move()
    if not moved:
        #render()
        print("Part 1:", i)
        break

data = open("input.data").read().strip().splitlines()

scan = {}
void = {}
wmm = [[0, 0, 0], [0, 0, 0]]
adjacents = [
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, -1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1)
]


def render(level=None):
    global scan, void
    if level is None:
        for z in range(wmm[1][2] + 1):
            for y in range(wmm[1][1] + 1):
                row = ""
                for x in range(wmm[1][0] + 1):
                    square = (x, y, z)
                    if square in scan:
                        row += "#"
                    else:
                        row += "."
                print(row)
    else:
        z = level
        print("Layer", z)
        for y in range(wmm[1][1] + 1):
            row = ""
            for x in range(wmm[1][0] + 1):
                square = (x, y, z)
                if square in scan:
                    row += "#"
                elif square in void:
                    row += "."
                else:
                    row += " "
            print(row)


def detect():
    global adjacents
    for z in range(wmm[1][2] + 1):
        for y in range(wmm[1][1] + 1):
            for x in range(wmm[1][0] + 1):
                square = (x, y, z)
                for adjacent in adjacents:
                    examine = (square[0] + adjacent[0], square[1] + adjacent[1], square[2] + adjacent[2])
                    if examine in scan:
                        if square in scan:
                            scan[square] -= 1


def detect2():
    global adjacents, scan, void

    traverse = [tuple(wmm[0])]

    while traverse:
        square = traverse.pop()
        # print("square", square)
        if square in void:
            continue

        void[square] = 0

        for adjacent in adjacents:
            neighbor = (square[0] + adjacent[0], square[1] + adjacent[1], square[2] + adjacent[2])
            if wmm[0][0] <= neighbor[0] <= wmm[1][0] and \
                    wmm[0][1] <= neighbor[1] <= wmm[1][1] and \
                    wmm[0][2] <= neighbor[2] <= wmm[1][2]:

                if neighbor in scan:
                    scan[neighbor] += 1
                else:
                    traverse.append(neighbor)


for line in data:
    x, y, z = line.split(",")
    cube = (int(x), int(y), int(z))
    scan[cube] = 6

    if cube[0] <= wmm[0][0]:
        wmm[0][0] = cube[0] - 1
    if cube[0] >= wmm[1][0]:
        wmm[1][0] = cube[0] + 1
    if cube[1] <= wmm[0][1]:
        wmm[0][1] = cube[1] - 1
    if cube[1] >= wmm[1][1]:
        wmm[1][1] = cube[1] + 1
    if cube[2] <= wmm[0][2]:
        wmm[0][2] = cube[2] - 1
    if cube[2] >= wmm[1][2]:
        wmm[1][2] = cube[2] + 1

detect()
print("Part 1:", sum(scan.values()))

for cube in scan.keys():
    scan[cube] = 0

detect2()
print("Part 2:", sum(scan.values()))

for level in range(wmm[1][2] + 1):
    render(level)
    input()

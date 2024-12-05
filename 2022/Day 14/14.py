data = open("input.data").read().strip().splitlines()

FALL = [(0, 1), (-1, 1), (1, 1)]
start = (500, 0)
edges = [(500, 0), (500, 1)]


def get_dir(a, b):
    h = v = 0
    if a[0] < b[0]:
        h = 1
    if a[0] > b[0]:
        h = -1
    if a[1] < b[1]:
        v = 1
    if a[1] > b[1]:
        v = -1

    return h, v


def draw_line(a, b):
    dir = get_dir(a, b)
    cur = a
    cave[cur] = '#'
    while cur != b:
        cur = (cur[0] + dir[0], cur[1] + dir[1])
        cave[cur] = '#'


def render(sand=None):
    global cave

    for y in range(edges[0][1], edges[1][1] + 1):
        row = ""
        for x in range(edges[0][0], edges[1][0]):
            coord = (x, y)
            if coord in cave:
                row += cave[coord]
            elif coord == sand:
                row += "+"
            else:
                row += '.'

        print(row)


def adjust_edges(point):
    global edges
    if point[0] < edges[0][0]:
        edges[0] = (point[0] - 1, edges[0][1])
    if point[0] > edges[1][0]:
        edges[1] = (point[0] + 1, edges[1][1])
    if point[1] < edges[0][1]:
        edges[0] = (edges[0][0], point[1] - 1)
    if point[1] > edges[1][1]:
        edges[1] = (edges[1][0], point[1] + 1)


def scan():
    for line in data:
        vertices = []
        for point in line.split(" -> "):
            x, y = point.split(",")
            point = (int(x), int(y))
            adjust_edges(point)
            vertices.append(point)

        prev = vertices.pop(0)
        while vertices:
            next = vertices.pop(0)
            draw_line(prev, next)
            prev = next


def part1():
    counter = 0
    abyss = False
    while not abyss:
        sand = start
        while True:
            prev = sand
            for next in [(sand[0] + f[0], sand[1] + f[1]) for f in FALL]:
                if next not in cave:
                    sand = next
                    break

            if sand[1] > edges[1][1]:
                abyss = True
                break

            if sand == prev:
                cave[sand] = 'o'
                counter += 1
                break

    return counter


def part2():
    counter = 0
    while start not in cave:
        sand = start
        while True:
            prev = sand
            for next in [(sand[0] + f[0], sand[1] + f[1]) for f in FALL]:
                if next not in cave:
                    sand = next
                    break

            if sand[1] == floor:
                prev = sand
                adjust_edges((sand[0] - 1, floor))
                adjust_edges((sand[0] + 1, floor))

            if sand == prev:
                cave[sand] = 'o'
                counter += 1
                break

    return counter


cave = {}
scan()
print("Part 1:", part1())

cave = {}
scan()
floor = edges[1][1]
adjust_edges((500, floor))
print("Part 2:", part2())

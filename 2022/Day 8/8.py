data = open("input.data").read().strip().splitlines()

width, height = [len(data[0]), len(data)]
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

visible = ((width - 1) * 2) + ((height - 1) * 2)
grid = {}

locations = []
for y in range(height - 1):
    locations.append((0, y, int(data[y][0])))

    for x in range(width - 1):
        current = int(data[y][x])
        if current > locations[-1][2]:
            locations.append((x, y, int(data[y][x])))

for y in range(height - 1):
    x = width - 1
    locations.append((x, y, int(data[y][x])))

    for x in range(width - 1, 0, -1):
        current = int(data[y][x])
        if current > locations[-1][2]:
            locations.append((x, y, int(data[y][x])))

for x in range(width - 1):
    locations.append((x, 0, int(data[0][x])))

    for y in range(height - 1):
        current = int(data[y][x])
        if current > locations[-1][2]:
            locations.append((x, y, int(data[y][x])))

for x in range(width - 1):
    y = height - 1
    locations.append((x, y, int(data[y][x])))

    for y in range(height - 1, 0, -1):
        current = int(data[y][x])
        if current > locations[-1][2]:
            locations.append((x, y, int(data[y][x])))

for tree in set(locations):
    if tree:
        grid[(tree[0], tree[1])] = tree[2]

visible = set()


def render(border=False, tree_house=None, viewline=False):
    global visible
    output = []
    for y in range(height):
        row = []
        for x in range(width):
            if border:
                if y == 0:
                    grid[(x, y)] = int(data[0][x])
                if y == height - 1:
                    grid[(x, y)] = int(data[height - 1][x])
                if x == 0:
                    grid[(x, y)] = int(data[y][0])
                if x == width - 1:
                    grid[(x, y)] = int(data[y][width - 1])

            if (x, y) in grid:
                row.append([str(grid[(x, y)]), "."][tree_house is not None])
                visible.add((x, y))
            else:
                row.append(" ")

        output.append(row)

    if tree_house:
        spot = tree_house[1]
        output[spot[1]][spot[0]] = "X"

        if viewline:
            for i in range(4):
                dir = [(0, -1), (1, 0), (0, 1), (-1, 0)][i]
                line = "|-|-"
                length = tree_house[2][i]
                view = (spot[0] + dir[0], spot[1] + dir[1])
                for j in range(length):
                    output[view[1]][view[0]] = line[i]
                    view = (view[0] + dir[0], view[1] + dir[1])

    for row in output:
        print("".join(row))


def count_trees(at, heading):
    count = 0
    coord = (at[0], at[1])
    tree = grid[at]
    while True:
        coord = (coord[0] + heading[0], coord[1] + heading[1])
        if coord[1] < 0 or coord[1] > height - 1 or coord[0] < 0 or coord[0] > width - 1:
            break

        looking_at = int(data[coord[1]][coord[0]])
        if looking_at < tree:
            count += 1
        else:
            count += 1
            break

    return count


def find_best_spot():
    spots = []
    best_spot = [0, None, None]
    for tree in visible:
        north = count_trees(tree, (0, -1))
        east = count_trees(tree, (1, 0))
        south = count_trees(tree, (0, 1))
        west = count_trees(tree, (-1, 0))
        spots.append(north * east * south * west)
        if spots[-1] > best_spot[0]:
            best_spot[0] = spots[-1]
            best_spot[1] = tree
            best_spot[2] = (north, east, south, west)

    return best_spot


render(True)
print("Part 1:", len(visible))
spot = find_best_spot()
print("Part 2:", spot[0])
render(False, spot, False)

data = open("input.data").read().strip().splitlines()

mm = {}
width = len(data[0])
height = len(data)
start = None
end = None

for y in range(height):
    for x in range(width):
        mm[(x, y)] = ord(data[y][x]) - 96
        if data[y][x] == "S":
            start = (x, y)
            mm[start] = 1
        elif data[y][x] == "E":
            end = (x, y)
            mm[end] = 26


def adjacents(coord):
    result = []
    for point in [(coord[0], coord[1] - 1), (coord[0] + 1, coord[1]), (coord[0], coord[1] + 1),
                  (coord[0] - 1, coord[1])]:
        if point[0] < 0 or point[1] < 0 or point[0] >= width or point[1] >= height:
            continue
        result.append(point)
    return result


def traverse(coord):
    dist = {}
    bfs = [(0, coord)]

    while len(bfs) > 0:
        t, p = bfs.pop(0)
        if p in dist:
            continue
        dist[p] = t

        for q in adjacents(p):
            if mm[q] - mm[p] > 1:
                continue
            bfs.append((t + 1, q))
    if end in dist:
        return dist[end]
    return None


print("Part 1:", traverse(start))

best = set()
starting_pos = []

for n in mm.keys():
    if mm[n] == 1:
        starting_pos.append(n)

for start in starting_pos:
    distance = traverse(start)
    if distance is None:
        continue

    best.add(distance)

print("Part 2:", sorted(best)[0])

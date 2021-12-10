"""

"""

inputdata = open("input.data").read().splitlines()

WIDTH = len(inputdata[0])
HEIGHT = len(inputdata)
ADJACENT = [(0, -1), (-1, 0), (1, 0), (0, 1)]

cave_map = []
risk_levels = []
low_points = []
basins = []

def find_adjacents(point):
    result = []
    for adjacent in ADJACENT:
        ax = point[0] + adjacent[0]
        ay = point[1] + adjacent[1]
        if ax < 0 or ax >= WIDTH or ay < 0 or ay >= HEIGHT:
            continue

        result.append((ax, ay, cave_map[ax + (ay * WIDTH)]))

    return result

#
#

for line in inputdata:
    cave_map.extend([int(x) for x in line])

for y in range(HEIGHT):
    for x in range(WIDTH):
        point = (x, y, cave_map[x + (y * WIDTH)])
        if point[2] < min(list(map(lambda x: x[2], find_adjacents(point)))):
            low_points.append(point)
            risk_levels.append(1 + point[2])

for low_point in low_points:
    basin = [low_point]
    new_points = [low_point]
    while len(new_points):
        point = new_points.pop()
        for adjacent in list(filter(lambda x: x[2] < 9 and x not in basin, find_adjacents(point))):
            basin.append(adjacent)
            new_points.append(adjacent)

    basins.append(len(basin))

basins = sorted(basins)[::-1]

print("Part 1:", sum(risk_levels))
print("Part 2:", basins[0] * basins[1] * basins[2])

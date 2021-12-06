"""

"""

inputdata = open("input.data").read().splitlines()

vent_map_1 = {}
vent_map_2 = {}

def parse_coord(data: str) -> (int, int):
    x, y = data.split(",")
    return (int(x), int(y))

def draw(vent_map: {}, x1, y1, x2, y2, diagonals=False):
    dir = stigningstall(x1, y1, x2, y2)
    if not diagonals and 0 not in dir:
        return
    xy = [x1, y1]
    while xy != [x2, y2]:
        plot(xy[0], xy[1], vent_map)
        xy[0] += dir[0]
        xy[1] += dir[1]
    plot(xy[0], xy[1], vent_map)

def plot(x: int, y: int, vent_map: {}):
    if (x, y) not in vent_map:
        vent_map[(x, y)] = 0
    vent_map[(x, y)] += 1 if (x, y) in vent_map else 1

def count_safe_areas(vent_map) -> int:
    return len(list(filter(lambda x: x > 1, vent_map.values())))

def stigningstall(x1, y1, x2, y2) -> (int, int):
    result = [0, 0]
    if x1 != x2:
        result[0] = 1 if x2 > x1 else -1
    if y1 != y2:
        result[1] = 1 if y2 > y1 else -1
    return result

for line in inputdata:
    a, b = line.split(" -> ")
    x1, y1 = parse_coord(a)
    x2, y2 = parse_coord(b)

    draw(vent_map_1, x1,y1, x2,y2)
    draw(vent_map_2, x1,y1, x2,y2, diagonals=True)

print("Part 1:", count_safe_areas(vent_map_1))
print("Part 2:", count_safe_areas(vent_map_2))

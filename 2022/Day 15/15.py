import math

data = open("input.data").read().strip().splitlines()

test = True
if test:
    data = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
""".strip().splitlines()

sensors = {}
beacons = {}
mapped = {}

edges = [(0, 0), (0, 0)]


def adjust_edges(coords=[]):
    global edges
    for coord in coords:
        if coord[0] < edges[0][0]:
            edges[0] = (coord[0], edges[0][1])
        if coord[0] > edges[1][0]:
            edges[1] = (coord[0] + 1, edges[1][1])
        if coord[1] < edges[0][1]:
            edges[0] = (edges[0][0], coord[1] - 1)
        if coord[1] > edges[1][1]:
            edges[1] = (edges[1][0], coord[1] + 1)


def render(s=None, b=None):
    global edges, mapped, sensors, beacons

    for y in range(edges[0][1], edges[1][1]):
        row = str(y).rjust(3, " ") + " "
        for x in range(edges[0][0], edges[1][0]):
            sensor = sensors.get((x, y), None)
            beacon = beacons.get((x, y), None)
            if s == (x, y):
                row += "1"
            elif b == (x, y):
                row += "2"
            elif sensor:
                row += ["s", "S"][sensor["beacon"] is not None]
            elif beacon:
                row += "B"
            elif (x, y) in mapped:
                row += mapped[(x, y)]
            else:
                row += "."
        print(row)
    print()


def distance(a, b) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


for line in data:
    line = line.replace("Sensor at x=", "").replace(" closest beacon is at x=", "").replace("y=", "")
    sensor, beacon = [eval(x) for x in line.split(":")]
    sensors[sensor] = {"beacon": beacon}
    beacons[beacon] = 1
    adjust_edges([sensor, beacon])

# find sensor/beacon lock signal
for beacon in beacons.keys():
    dists = {}
    for i, sensor in enumerate(sensors.keys()):
        dist = distance(sensor, beacon)
        dists[dist] = (sensor, beacon)

    nearest = sorted(dists.keys())
    s, b = dists[nearest[0]]

    sensors[s]["beacon"] = b


def get_nearest_beacon(coord):
    global beacons
    dists = {}
    for b in beacons.keys():
        dist = distance(coord, b)
        dists[dist] = (coord, b)
    nearest = sorted(dists.keys())
    return dists[nearest[0]][1]


def p1(row=10):
    global beacons, edges, sensors, mapped
    counter = 0
    for s in sensors.keys():
        b = sensors[s]["beacon"]

        dist = distance(s, b)
        area = [(s[0] - dist, s[1] - dist), (s[0] + dist, s[1] + dist)]
        y = row
        for x in range(area[0][0], area[1][0]):
            if (x, y) in sensors or (x, y) in beacons or (x, y) in mapped:
                continue

            delta = distance(s, (x, y))
            if delta <= dist:
                mapped[(x, y)] = "#"
                if y == row:
                    counter += 1

    return counter


def p2(top=20):
    global beacons, edges, sensors, mapped

    # for s in sensors.keys():
    #    b = sensors[s]["beacon"]
    #    dist = distance(s, b)
    #    area = [(s[0] - dist, s[1] - dist), (s[0] + dist, s[1] + dist)]
    #
    #    for x in range(area[0][0], area[1][0]):
    #        for y in range(area[0][1], area[1][1]):
    #            if distance(s, (x, y)) > dist:
    #                continue
    #            mapped[(x, y)] = "#"

    for s in sensors.keys():
        b = sensors[s]["beacon"]

        dist = distance(s, b) + 1
        area = [(s[0] - dist, s[1] - dist), (s[0] + dist, s[1] + dist)]
        print(area)

        for x in range(area[0][0], area[1][0]):
            for y in range(area[0][1], area[1][1]):
                delta = distance(s, (x, y))
                if delta != dist:
                    continue
                if x < 0 or x >= top or y < 0 or y >= top:
                    continue
                if inside_another((x, y)):
                    print("inside")
                    continue
                # if (x, y) in sensors or (x, y) in beacons or (x, y) in mapped:
                #    continue
                print("What?", (x, y))
                return x * 4000000 + y


def inside_another(p) -> bool:
    inside = False
    print(50 * ".")
    print("Checking point", p)
    for s in sensors.keys():
        b = sensors[s]["beacon"]

        dist = distance(s, b)
        sum_rect = dist * dist
        print("Sum Rectangle:", sum_rect, "at", s, "with size", dist)

        a = (s[0] - dist, s[1])
        b = (s[0], s[1] - dist)
        c = (s[0] + dist, s[1])
        d = (s[0], s[1] + dist)
        sum_apd = get_sum(p, a, d)
        sum_apb = get_sum(p, a, b)
        sum_bpc = get_sum(p, b, c)
        sum_cpd = get_sum(p, c, d)

        delta_apd = (distance(a, p), distance(p, d), distance(d, a))
        delta_apb = (distance(a, p), distance(p, b), distance(b, a))
        delta_bpc = (distance(b, p), distance(p, c), distance(c, b))
        delta_cpd = (distance(c, p), distance(p, d), distance(d, c))

        print("p", p)
        print("a", a)
        print("b", b)
        print("c", c)
        print("d", d)
        print(delta_apd)
        print(delta_apb)
        print(delta_bpc)
        print(delta_cpd)
        print()
        print(sum_apd, ">", sum_rect, dist)
        print(sum_apd, sum_apb, sum_bpc, sum_cpd, "  =>  ", sum([sum_apd, sum_apb, sum_bpc, sum_cpd]), "<", sum_rect)
        if sum([sum_apd, sum_apb, sum_bpc, sum_cpd]) <= sum_rect:
            inside = True
            print("inside...")
            break
        input()
    return inside


def get_sum(a, b, c):
    x = [a[0], b[0], c[0]]
    y = [a[1], b[1], c[1]]
    return abs(int(0.5 * ((x[0] * (y[1] - y[2])) + (x[1] * (y[2] - y[0])) + (x[2] * (y[0] - y[1])))))

    print("get sum:", a, b, c, "=>",
          abs((b[0] * a[1] - a[0] * b[1]) + (c[0] * b[1] - b[0] * c[1]) + (a[0] * c[1] - c[0] * a[1])) / 2)
    return abs((b[0] * a[1] - a[0] * b[1]) + (c[0] * b[1] - b[0] * c[1]) + (a[0] * c[1] - c[0] * a[1])) / 2


# print("Part 1:", p1([2000000, 10][test]))

# if test:
#    render()

p = p2([4000000, 20][test])
print("Part 2:", p)
# if test:
#    render()

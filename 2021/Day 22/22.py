from itertools import permutations

inputdata = open("input.data").read().strip().splitlines()

inputdata = """
on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10
""".strip().splitlines()

reactor = set()

x_lo = 0
x_hi = 0
y_lo = 0
y_hi = 0

for line in inputdata:
    state, data = line.split(" ")
    data = data.split(",")

    x1, x2 = data[0][2:].split("..")
    y1, y2 = data[1][2:].split("..")
    z1, z2 = data[2][2:].split("..")

    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    z1 = int(z1)
    z2 = int(z2)

    if x1 < x_lo:
        x_lo = x1
    if x2 > x_hi:
        x_hi = x2
    if y1 < y_lo:
        y_lo = y1
    if y2 > y_hi:
        y_hi = y2

    x1 = max(-50, x1)
    x2 = min( 50, x2)
    y1 = max(-50, y1)
    y2 = min( 50, y2)
    z1 = max(-50, z1)
    z2 = min( 50, z2)

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):
                if state == "on":
                    reactor.add((x, y, z))
                elif (x, y, z) in reactor:
                    reactor.remove((x, y, z))

#

print("Part 1:", len(reactor))

print(x_lo, x_hi, "-", y_lo, y_hi)
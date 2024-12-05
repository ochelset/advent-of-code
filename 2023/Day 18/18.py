import itertools
from collections import Counter

data = open("input.data").read().strip().split("\n")

test_data = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
""".strip().split("\n")

data = test_data

coords = {}

coord = (0,0)
start = (0,0)
width = 0
height = 0
first = (0,0)

#points = [(0, 0)]
#dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
#b = 0
#for line in data:
#    d, n, _ = line.split()
#    dr, dc = dirs[d]
#    n = int(n)
#    b += n
#    r, c = points[-1]
#    points.append((r + dr * n, c + dc * n))

#A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
#i = A - b // 2 + 1
#print(i + b)
#input()

prev = None
for line in data:
    dir, length, color = line.split(" ")
    color = color.replace('(#', '').replace(')', '')

    if coord not in coords:
        coords[coord] = { "m": dir, "c": int(color, 16), "p": prev }
        prev = coord

    for i in range(int(length)):
        if dir == "R":
            coord = (coord[0]+1, coord[1])
        elif dir == "L":
            coord = (coord[0]-1, coord[1])
        elif dir == "U":
            coord = (coord[0], coord[1]-1)
        elif dir == "D":
            coord = (coord[0], coord[1]+1)

        if coord in coords:
            continue

        coords[coord] = { "m": dir, "c": int(color, 16), "p": prev }
        coords[prev]["next"] = coord
        prev = coord

        if coord[0] > width:
            width = coord[0]
        if coord[1] > height:
            height = coord[1]
        if coord[0] < start[0]:
            start = (coord[0], start[1])
        if (coord[1] < start[1]):
            start = (start[0], coord[1])

width += 1
height += 1
result = len(coords.keys())
inside = (0,0)
print(coords)
#print(coords[first])
#dir = (coords[first]["next"][0]-first[0], coords[first]["next"][1]-first[1])
dir = (0, 1)
#print("----")
inside = {}
next = (0,0)
prev = coords[first]["m"]
finished = False
while not finished:
    current = coords[next]
    x, y = next

    #print("Going", current["m"])
    if current["m"] != prev:
        #print("Rotate dir", dir)
        m = [0, 1, -1, 0]
        if prev == "R" and current["m"] == "D":
            m = [0, -1, 1, 0]
        elif prev == "D" and current["m"] == "L":
            m = [0, -1, 1, 0]
        elif prev == "L" and current["m"] == "U":
            m = [0, -1, 1, 0]
        elif prev == "U" and current["m"] == "R":
            m = [0, -1, 1, 0]

        dir = (dir[0]*m[0] + dir[1]*m[1], dir[0]*m[2]+dir[1]*m[3])
        prev = current["m"]
        #print("NEW DIR", dir, m)
        #input()

    #

    check = (x, y)
    while True:
        check = (check[0]+dir[0], check[1]+dir[1])
        #print("CHECKING", check, prev)
        if check in coords:
            #print("Hit")
            if "next" not in current:
                finished = True
                break
            next = current["next"]
            #input()
            break

        inside[check] = True
        #input()

for y in range(start[1]-1, height+1):
    row = ''
    on = False
    for x in range(start[0]-1, width+1):
        if (x, y) in coords:
            row += '#'
            on = not on
            continue
        elif (x, y) in inside:
            result += 1
            row += "#"
        else:
            row += "."

    if False:
        print(row)

print("Part 1:", result) # 70025 too low
#print(inside)
import math

inputdata = open("input.data").read().strip().split("\n\n")
inputdata = """
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
""".strip().split("\n\n")

tiles = {}
images = {}
SIZE = int(math.sqrt(len(inputdata)))

def binary(data: str):
    return "".join(["1" if x == "#" else "0" for x in data])

def render(image):
    for row in image:
        print("".join(row))
    print()

def match(source):
    result = {
        "tile": source,
        "neighbors": {},
        "orientation": 0,
        "flipped": 0
    }

    for id, tile in tiles.items():
        if id == source:
            continue

        sides = set(tiles[source]).intersection(tile)
        if len(sides) > 0:
            #print(source, "<->", id)
            #print(source, tiles[source])
            #print(id, tile)
            #print(sides)
            #print()

            for side in sides:
                result["neighbors"][tiles[source].index(side)] = id
            #print(result)
            #input()
    return result

#

for tile in inputdata:
    #print(tile)
    tile = tile.splitlines()
    id = int(tile.pop(0).replace("Tile ", "").replace(":", ""))
    images[id] = tile[:]
    top = binary(tile[0])
    top_flipped = top[::-1]
    bottom = binary(tile[-1])
    bottom_flipped = bottom[::-1]
    left = binary("".join([x[0] for x in tile]))
    left_flipped = left[::-1]
    right = binary("".join([x[-1] for x in tile]))
    right_flipped = right[::-1]

    tile = (int(top, base=2), int(right, base=2), int(bottom, base=2), int(left, base=2),
            int(bottom_flipped, base=2), int(left_flipped, base=2), int(top_flipped, base=2), int(right_flipped, base=2))
    tiles[id] = tile
    #print("Tile", id)
    #print(top, right, bottom, left)
    #print(top_flipped, right_flipped, bottom_flipped, left_flipped)
    #print(tile)
    #input()

corners = []
placed = {}

for id in tiles.keys():
    current = tiles[id]
    sides = 0

    for t_id, tile in tiles.items():
        if t_id == id:
            continue

        if len(set(current).intersection(tile)) == 2:
            sides += 1

    if sides == 2:
        corners.append(id)

print("Part 1:", math.prod(corners))
print(80*"-")
print("CORNERS:", corners)
print()

scanned = []
for i in range(4):
    scanned = [0] * SIZE * SIZE
    scanned[0] = corners[i]

    for y in range(SIZE):
        for x in range(SIZE):
            index = y * SIZE + x
            if scanned[index] != 0:
                continue

            #print("At", (x, y))
            for pos in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                neighbor = (x + pos[0], y + pos[1])
                if neighbor[0] < 0 or neighbor[0] >= SIZE or neighbor[1] < 0 or neighbor[1] >= SIZE:
                    continue

                n_index = neighbor[1] * SIZE + neighbor[0]
                if scanned[n_index] == 0:
                    #if scanned[0] == 3851:
                    #    print((x, y), "has an neighbor that is empty", neighbor)
                    continue
                #print("NEIGHBORS", pos, neighbor, n_index, scanned[n_index])

                matching = match(scanned[n_index])
                #if scanned[0] == 3851:
                #    print("MATCHING", pos, matching)

                if pos == (-1, 0):
                    #if scanned[0] == 3851:
                    #    print("FIND LEFT/RIGHT EDGE")
                    if 1 in matching["neighbors"] or 7 in matching["neighbors"]:
                        scanned[index] = matching["neighbors"][1]
                    elif 3 in matching["neighbors"] or 5 in matching["neighbors"]:
                        scanned[index] = matching["neighbors"][3]
                        #print("GOT A MATCH", matching["tile"], matching["neighbors"][1])

                elif pos == (0, -1):
                    #if scanned[0] == 3851:
                    #    print("FIND TOP/BOTTOM EDGE")
                    if 0 in matching["neighbors"] or 6 in matching["neighbors"]:
                        scanned[index] = matching["neighbors"][0]
                    elif 2 in matching["neighbors"] or 4 in matching["neighbors"]:
                        scanned[index] = matching["neighbors"][2]
                        #print("GOT A MATCH", matching["tile"], matching["neighbors"][0])

    if 0 not in scanned:
        break

#print(scanned)
for y in range(SIZE):
    row = []
    for i in range(10):
        for x in range(SIZE):
            index = y * SIZE + x
            id = scanned[index]
            image = images[id]
            row.append(image[i])
    print(row)

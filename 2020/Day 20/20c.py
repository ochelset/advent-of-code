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
    scanned = [None] * SIZE * SIZE
    scanned[0] = (corners[i], 0, 0)

    # FIGURE OUT orientation of top left corner first
    matching_corner = match(corners[i])
    print(matching_corner)

    tile = tiles[corners[i]]
    print("TILE  ", tile)
    if 1 in matching_corner["neighbors"] or 7 in matching_corner["neighbors"]:
        poss = tiles[matching_corner["neighbors"][1]]
        print("POSS SIDES", poss, poss.index(tile[1]))

    if 0 in matching_corner["neighbors"] or 6 in matching_corner["neighbors"]:
        poss = tiles[matching_corner["neighbors"][0]]
        print("POSS TOP/B", poss, poss.index(tile[0]))

        if poss.index(tile[0]) == 2:
            scanned[0] = (corners[i], 0, 1)

    print(scanned)
    input()
    continue


    for y in range(SIZE):
        for x in range(SIZE):
            index = y * SIZE + x
            if scanned[index] != None:
                continue

            print("At", (x, y))
            for pos in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                neighbor = (x + pos[0], y + pos[1])
                if neighbor[0] < 0 or neighbor[0] >= SIZE or neighbor[1] < 0 or neighbor[1] >= SIZE:
                    continue

                n_index = neighbor[1] * SIZE + neighbor[0]
                if scanned[n_index] == None:
                    continue

                print("NEIGHBORS", neighbor, n_index, scanned[n_index])
                matching = match(scanned[n_index][0])
                print("MATCHING", pos, matching)

                id = 0
                rotation = 0
                flipped = 0

                n_rotation = scanned[n_index][1]
                n_flipped = scanned[n_index][2]

                if pos == (-1, 0):
                    n_tile = tiles[matching["tile"]]
                    print("NEIGHBOR", n_tile[:4])
                    print("FIND LEFT/RIGHT EDGE")
                    if 1 in matching["neighbors"] or 7 in matching["neighbors"]:
                        id = matching["neighbors"][1]
                        tile = tiles[id]
                        print("CURRENT ", tile)
                        print("A", tile.index(n_tile[1]))
                        print("B", tile.index(n_tile[7]))
                        if tile.index(n_tile[1]) == 5:
                            flipped = 2
                    elif 3 in matching["neighbors"] or 5 in matching["neighbors"]:
                        id = matching["neighbors"][3]
                        #print("GOT A MATCH", matching["tile"], matching["neighbors"][1])

                elif pos == (0, -1):
                    n_tile = tiles[matching["tile"]]
                    print("NEIGHBOR", n_tile[:4])
                    print("FIND TOP/BOTTOM EDGE")
                    if 0 in matching["neighbors"] or 6 in matching["neighbors"]:
                        id = matching["neighbors"][0]
                        tile = tiles[id]
                        print("CURRENT ", tile)
                        print("A", tile.index(n_tile[0]))
                        print("B", tile.index(n_tile[6]))
                    elif 2 in matching["neighbors"] or 4 in matching["neighbors"]:
                        id = matching["neighbors"][2]
                        #print("GOT A MATCH", matching["tile"], matching["neighbors"][0])
                input()
                scanned[index] = (id, rotation, flipped)

    if None not in scanned:
        break

print()
print(scanned)
print()

for scan in scanned:
    if scan[2] == 2: # FLIP VERTICALLY
        images[scan[0]] = images[scan[0]][::-1]

for y in range(SIZE):
    row = ""

    for i in range(10):
        for x in range(SIZE):
            index = y * SIZE + x
            id = scanned[index][0]
            image = images[id]
            row += image[i]
            row += " "
        row += "\n"
    print(row)

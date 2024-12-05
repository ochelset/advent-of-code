import itertools

data = open("input.data").read().strip().split("\n")

test_data = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip().split("\n")

xdata = test_data

def find_galaxies(data):
    result = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "#":
                result.append({ "x": x, "y": y })
    return result

def expand_universe(galaxies, size=1):
    size -= 1
    for y in range(len(data)):
        if data[y].find('#') == -1:
            for galaxy in galaxies:
                if galaxy["y"] < y:
                    galaxy["y"] -= size

    for x in range(len(data[0])):
        empty = True
        for y in range(len(data)):
            if data[y][x] == "#":
                empty = False
                break

        if empty:
            for galaxy in galaxies:
                if galaxy["x"] < x:
                    galaxy["x"] -= size

    return galaxies

def distance(a, b) -> int:
    return abs(b["x"] - a["x"]) + abs(b["y"] - a["y"])

##
##

for i, expansion in enumerate([2, 1000000]):
    galaxies = expand_universe(find_galaxies(data), expansion)
    pairs = itertools.combinations(galaxies, 2)

    result = 0
    for pair in pairs:
        d = distance(pair[0], pair[1])
        result += d

    print("Part %s:" % (i+1), result) #1: 9543156 2: 625243292686
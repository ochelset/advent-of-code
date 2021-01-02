CENTER = (0, 0, 0)

data = open("input.data").read().strip().split("\n")

testdata = """
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
""".strip().split("\n")


class Floor():
    tiles: dict

    def __init__(self):
        self.tiles = {}
        self.add_tile(0, 0)

    def add_tile(self, i: int, j: int):
        self.tiles[(i, j)] = True

    def move_to(self, route: list):
        position = CENTER
        for dir in route:
            if dir == "nw":
                position = (position[0], position[1] - 1)
            elif dir == "ne":
                position = (position[0] + 1, position[1] - 1)
            elif dir == "e":
                position = (position[0] + 1, position[1])
            elif dir == "se":
                position = (position[0], position[1] + 1)
            elif dir == "sw":
                position = (position[0] - 1, position[1] + 1)
            elif dir == "w":
                position = (position[0] - 1, position[1])

            if not position in self.tiles:
                self.add_tile(position[0], position[1])

        self.tiles[position] = not self.tiles[position]

    def daily_flip(self):
        minx, maxx = 0, 0
        miny, maxy = 0, 0
        for position in self.tiles.keys():
            if self.tiles[position] == True:
                minx = min(minx, position[0]-2)
                miny = min(miny, position[1]-2)
                maxx = max(maxx, position[0]+2)
                maxy = max(maxy, position[1]+2)

        for y in range(miny, maxy):
            for x in range(minx, maxx):
                if (x, y) not in self.tiles:
                    self.tiles[(x, y)] = True

        new_tiles = self.tiles.copy()
        tiles = list(self.tiles.keys())
        for position in tiles:
            tile = self.tiles[position]
            black_neighbors = self.black_neighbors(position, new_tiles)

            if not tile and black_neighbors not in [1, 2]:
                new_tiles[position] = True
            elif tile and black_neighbors == 2:
                new_tiles[position] = False

        self.tiles = new_tiles.copy()

    def black_neighbors(self, position: tuple, new_tiles: dict) -> int:
        count = 0
        for neighbor in [(0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]:
            neighbor_pos = (position[0] + neighbor[0], position[1] + neighbor[1])
            if not neighbor_pos in self.tiles:
                new_tiles[(neighbor_pos[0], neighbor_pos[1])] = True
                continue

            if self.tiles[neighbor_pos] == False:
                count += 1
        return count

    def count(self) -> int:
        return len(list(filter(lambda x: self.tiles[x] == False, self.tiles)))

def parse_route(route: str) -> list:
    result = []
    while route:
        if route[0] == "e" or route[0] == "w":
            result.append(route[0])
            route = route[1:]
        else:
            result.append(route[:2])
            route = route[2:]

    return result

def part1(data: list):
    floor = Floor()

    for route in data:
        route = parse_route(route)
        floor.move_to(route)

    print("Part 1:", floor.count())

    for day in range(1, 101):
        floor.daily_flip()

    print("Part 2:", floor.count())


part1(data)

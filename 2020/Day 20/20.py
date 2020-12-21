import math

testdata = """Tile 2311:
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
..#.###..."""

class Connection():
    a: str
    b: str

class TileImage():
    id: int
    data: list
    image: list
    edges: list
    flipped_edges: list
    orientation: 0
    flipped: 0
    x: None
    y: None
    top: None
    right: None
    bottom: None
    left: None
    locked = False
    connections: list

    def __init__(self, data: str):
        self.image = []
        self.edges = []
        self.flipped_edges = []
        self.orientation = 0
        self.flipped = 0
        self.x = None
        self.y = None
        self.top = None
        self.right = None
        self.bottom = None
        self.left = None
        self.locked = False
        self.connections = []

        self.convert(data)
        self.find_edges()

    def convert(self, data: str):
        data = data.strip().split("\n")
        self.id = int(data[0][5:-1])
        self.data = data[1:]
        for line in self.data:
            line = int(line.replace(".", "0").replace("#", "1"), 2)
            self.image.append(line)

    def find_edges(self):
        TOP = self.image[0]
        LEFT = ""
        RIGHT = ""
        BOTTOM = self.image[-1]

        for line in self.image:
            line = bin(line)[2:].rjust(10, "0")
            LEFT += str(line[0])
            RIGHT += str(line[-1])

        LEFT = int(LEFT, 2)
        RIGHT = int(RIGHT, 2)

        self.edges = [TOP, LEFT, BOTTOM, RIGHT]

        # find rotated edges
        for edge in self.edges[:4]:
            flipped_edge = bin(edge)[2:].rjust(10, "0")[::-1]
            self.edges.append(int(flipped_edge, 2))

            # 0 = top
            # 1 = right
            # 2 = bottom
            # 3 = left
            # 4 = bottom (flipped)
            # 5 = left (flipped)
            # 6 = top (flipped)
            # 7 = right (flipped)

        #print("FOUND EDGES for", self.id, self.edges)

    def connect(self, image):
        edges = set(self.edges).intersection(image.edges)
        #print("Connect", self.id, "->", image.id)
        while edges:
            edge = edges.pop()
            #print("Edge:", edge)
            mine = self.edges.index(edge)
            self.connections.append((image.id, mine))

        #print("Connected", self.connections)

    def render(self):
        print()
        print("Tile", self.id, self.orientation, self.flipped)
        data = self.data[:]
        data = self.rotate_data(data)
        data = self.flip_data(data)
        for line in data:
            print(line)

    def rotate_data(self, data) -> list:
        #print("ROTATE", self.orientation, len(data))
        size = len(data)
        output = data[:]
        #print(output)

        if self.orientation > 0:
            orientation = self.orientation
            while orientation:
                output = [[[] * size for i in range(size)] for j in range(size)]
                for y, line in enumerate(data):
                    for x, char in enumerate(line):
                        output[x][size-y-1] = char

                for i, o in enumerate(output):
                    output[i] = "".join(o)

                data = output[:]
                orientation -= 90

        return output

    def flip_data(self, data: list) -> list:
        size = len(data)
        if self.flipped == 1: # Vertical flip
            return data[::-1]
        elif self.flipped == 2: # Horizontal flip
            output = []
            for line in data:
                output.append(line[::-1])
            return output

        return data

def analyze(tiles: list) -> dict:
    images = {}
    for tile in tiles:
        tile_image = TileImage(tile)
        images[tile_image.id] = tile_image

    return images

def organize_tiles(images: dict, corners: list):
    print("ORGANIZE", corners)

    images[corners[0]].render()
    images[corners[0]].orientation = 90
    images[corners[0]].render()
    images[corners[0]].orientation = 180
    images[corners[0]].render()
    images[corners[0]].orientation = 270
    images[corners[0]].render()
    print()
    print("--")
    images[corners[0]].orientation = 0
    images[corners[0]].render()
    images[corners[0]].flipped = 1
    images[corners[0]].render()
    images[corners[0]].flipped = 2
    images[corners[0]].render()


def part1(data: str):
    tiles = data.split("\n\n")
    images = analyze(tiles)

    image_list = [images[n] for n in images.keys()]

    for i in range(len(image_list)):
        examine = image_list[i]
        edges = set(examine.edges)
        #print("START", examine.id, examine.edges)
        for image in image_list:
            if image.id == examine.id:
                continue

            if edges.intersection(image.edges):
                examine.connect(image)

    corners = []
    shortest = 100
    for id in images.keys():
        connections_length = len(images[id].connections)
        if connections_length < shortest:
            shortest = len(images[id].connections)
            corners = []
        if connections_length == shortest:
            corners.append(id)

        #print("**", id, images[id].connections)

    result = 1
    for corner in corners:
        result *= corner

    print("Part 1:", result)

    organize_tiles(images, corners)
    #remove_borders()
    #remove_spacing()
    #find_monsters()

data = open("input.data").read().strip()

part1(testdata)
#part1(data)
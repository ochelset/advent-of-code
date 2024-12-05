data = open("input.data").read().strip().split("\n")
from shapely.geometry import Point, Polygon

def is_point_inside_polygon(x, y, polygon):
    point = Point(x, y)
    return point.within(polygon)

class Pipe:
    pos = None
    pipe_in = None
    pipe_out = None

    def __init__(self, pos=None, pipe=None) -> None:
        self.pos = pos
        self.pipe_out = None

        if pipe:
            if pipe.pipe_out == 'N':
                self.pipe_in = 'S'
            if pipe.pipe_out == 'E':
                self.pipe_in = 'W'
            if pipe.pipe_out == 'S':
                self.pipe_in = 'N'
            if pipe.pipe_out == 'W':
                self.pipe_in = 'E'

            if self.pipe_in == 'N':
                if self.pos[2] == '|':
                    self.pipe_out = 'S'
                if self.pos[2] == 'J':
                    self.pipe_out = 'W'
                if self.pos[2] == 'L':
                    self.pipe_out = 'E'

            if self.pipe_in == 'E':
                if self.pos[2] == '-':
                    self.pipe_out = 'W'
                if self.pos[2] == 'F':
                    self.pipe_out = 'S'
                if self.pos[2] == 'L':
                    self.pipe_out = 'N'

            if self.pipe_in == 'S':
                if self.pos[2] == '|':
                    self.pipe_out = 'N'
                if self.pos[2] == '7':
                    self.pipe_out = 'W'
                if self.pos[2] == 'F':
                    self.pipe_out = 'E'

            if self.pipe_in == 'W':
                if self.pos[2] == '-':
                    self.pipe_out = 'E'
                if self.pos[2] == 'J':
                    self.pipe_out = 'N'
                if self.pos[2] == '7':
                    self.pipe_out = 'S'

    #
    #

    def next(self):
        if self.pipe_out == 'N':
            return (self.pos[0], self.pos[1]-1)
        if self.pipe_out == 'E':
            return (self.pos[0]+1, self.pos[1])
        if self.pipe_out == 'S':
            return (self.pos[0], self.pos[1]+1)
        if self.pipe_out == 'W':
            return (self.pos[0]-1, self.pos[1])

test_data = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
""".strip().split("\n")

data = test_data

def find_start():
    start = None
    for y in range(len(data)):
        if start != None:
            break
        for x in range(len(data[y])):
            if data[y][x] == 'S':
                start = (x, y)
                break

    nn = (start[0], start[1]-1, 'N')
    en = (start[0]+1, start[1], 'E')
    sn = (start[0], start[1]+1, 'S')
    wn = (start[0]-1, start[1], 'W')

    possibles = {
        'NS': '|',
        'EW': '-',
        'NE': 'L',
        'ES': 'F',
        'WS': '7',
        'WN': 'J'
    }

    valids = ''
    for neighbor in [wn, nn, en, sn]:
        if neighbor[0] < 0 or neighbor[0] > len(data[0]) or neighbor[1] < 0 or neighbor[1] > len(data):
            continue

        tile = data[neighbor[1]][neighbor[0]]
        #print(">", start, neighbor, tile)
        if tile == ".":
            continue

        if neighbor[2] == "N" and tile in '|7F':
            valids += 'N'
        if neighbor[2] == "S" and tile in '|LJ':
            valids += 'S'
        if neighbor[2] == "E" and tile in '-7J':
            valids += 'E'
        if neighbor[2] == "W" and tile in '-LF':
            valids += 'W'

    return (start[0], start[1], possibles[valids])

def render(steps):
    for y in range(len(data)):
        row = []
        for x in range(len(data[0])):
            t = data[y][x]
            if (x, y) in steps:
                row.append('*')
                #row.append(t)
            else:
                row.append(t)
        print(''.join(row))
#
#

pipeline = []
start = find_start()
p = Pipe(start)
pipeline.append(p)
print(start)
if start[2] == 'F':
    p.pipe_in = 'S'
    p.pipe_out = 'E'
if start[2] == '|':
    p.pipe_in = 'S'
    p.pipe_out = 'N'
if start[2] == '7':
    p.pipe_in = 'S'
    p.pipe_out = 'W'

steps = []
steps.append((p.pos[0], p.pos[1]))
while True:
    next_pos = p.next()
    tile = data[next_pos[1]][next_pos[0]]
    if tile == "S":
        print("Part 1:", round(len(steps) / 2))
        break

    pp = Pipe((next_pos[0], next_pos[1], tile), p)
    pipeline.append(pp)

    steps.append((next_pos[0], next_pos[1]))
    p = pp

    #render(steps)
    #input()

#print("STEPS", len(steps))

polygon = Polygon(steps[::-1])

inside = 0
outside = 0
buffer = []
for y in range(len(data)):
    row = []
    for x in range(len(data[0])):
        t = data[y][x]
        if (x, y) in steps:
            #row.append('*')
            row.append(t)
        else:
            row.append('I')
    buffer.append(row)
    print(''.join(row))

outside = set()

def check(pipe, dir=(0,0)):
    for pos in range(1, 4):
        p = (pipe.pos[0]+dir[0], pipe.pos[1]+dir[1])
        if p in steps:
            continue
        outside.add(p)
        print(pipe.pos, '+', p,  outside)

for pipe in pipeline:
    if pipe.pipe_in == 'S' and pipe.pipe_out == 'E':
        check(pipe, (-1, 0))
    if pipe.pipe_in == 'S' and pipe.pipe_out == 'N':
        check(pipe, (-1, 0))
    if pipe.pipe_in == 'S' and pipe.pipe_out == 'W':
        check(pipe, (1, 0))

print("Part 2:", inside)
print(outside)
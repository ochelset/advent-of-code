inputdata = """
1254117228
4416873224
8354381553
1372637614
5586538553
7213333427
3571362825
1681126243
8718312138
5254266347
"""

WIDTH = 10
HEIGHT = 10
ADJACENT = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

octopus = [int(x) for x in inputdata.replace("\n", "")]

def increase():
    for i in range(WIDTH*HEIGHT):
        octopus[i] += 1

def increase_neighbors(pos):
    for adjacent in ADJACENT:
        adj_pos = (pos[0] + adjacent[0], pos[1] + adjacent[1])
        if adj_pos[0] < 0 or adj_pos[0] >= WIDTH or adj_pos[1] < 0 or adj_pos[1] >= HEIGHT:
            continue

        i = adj_pos[1] * WIDTH + adj_pos[0]
        if octopus[i] > 9:
            continue

        octopus[i] += 1

def flash():
    have_flashed = set()
    while 10 in octopus:
        flashed = []
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if octopus[y*WIDTH + x] > 9 and (x, y) not in have_flashed:
                    flashed.append((x, y))

        while flashed:
            pos = flashed.pop()
            if pos in have_flashed:
                continue
            octopus[pos[1]*WIDTH+pos[0]] = 11
            have_flashed.add(pos)
            increase_neighbors(pos)

def reset():
    global octopus
    octopus = list(map(lambda x: 0 if x > 9 else x, octopus))

flashes = 0
i = 0
while True:
    i += 1
    increase()
    flash()
    reset()

    flashes += len(list(filter(lambda x: x == 0, octopus)))

    if i == 100:
        print("Part 1:", flashes)

    if sum(octopus) == 0:
        print("Part 2:", i)
        break

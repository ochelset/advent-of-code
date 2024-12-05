data = open("input.data").read().strip().split("\n")
test_data = open("test.data").read().strip().split("\n")

xdata = test_data

width = len(data[0])
height = len(data)

tiles = {}
lights = [{ "pos": (-1, 0), "dir":(1, 0) }]
energized = set()

def move(light):
    light["pos"] = (light["pos"][0] + light["dir"][0], light["pos"][1] + light["dir"][1])

for y in range(height):
    for x in range(width):
        if data[y][x] != ".":
            tiles[(x, y)] = data[y][x]

def find_energy(lights):
    beamed = set()
    while lights:
        l = len(lights)
        new_lights = []
        for i in range(l):
            light = lights[i]
            move(light)
            if light["pos"][0] >= 0 and light["pos"][0] < width and light["pos"][1] >= 0 and light["pos"][1] < height and light["pos"]:
                if (light["pos"][0], light["pos"][1], light["dir"][0], light["dir"][1]) not in energized:
                    new_lights.append(light)
            else:
                continue

            beamed.add(light["pos"])
            energized.add((light["pos"][0], light["pos"][1], light["dir"][0], light["dir"][1]))
            if light["pos"] in tiles:
                tile = tiles[light["pos"]]
                if tile == "|" and light["dir"][0] != 0:
                    light["dir"] = (0, -1)
                    new_lights.append({ "pos": light["pos"], "dir":(0,1) })
                if tile == "-" and light["dir"][1] != 0:
                    light["dir"] = (-1, 0)
                    new_lights.append({ "pos": light["pos"], "dir":(1,0) })

                if tile == "/":
                    if light["dir"][0] == 1:
                        light["dir"] = (0, -1)
                    elif light["dir"][0] == -1:
                        light["dir"] = (0, 1)
                    elif light["dir"][1] == 1:
                        light["dir"] = (-1, 0)
                    elif light["dir"][1] == -1:
                        light["dir"] = (1, 0)

                if tile == "\\":
                    if light["dir"][0] == 1:
                        light["dir"] = (0, 1)
                    elif light["dir"][0] == -1:
                        light["dir"] = (0, -1)
                    elif light["dir"][1] == 1:
                        light["dir"] = (1, 0)
                    elif light["dir"][1] == -1:
                        light["dir"] = (-1, 0)

        lights = new_lights

    return len(list(beamed))

print("Part 1:", find_energy(lights))

top = (0, 0)
bottom = (0, height)
left = (0, 0)
right = (width, 0)

max_energy = 0

#top->down
for x in range(width):
    energized = set()
    lights = [{ "pos": (x, -1), "dir":(0, 1) }]
    energy = find_energy(lights)
    if energy > max_energy:
        max_energy = energy

#bottom->up
for x in range(width):
    energized = set()
    lights = [{ "pos": (x, height), "dir":(0, -1) }]
    energy = find_energy(lights)
    if energy > max_energy:
        max_energy = energy

#left->right
for y in range(height):
    energized = set()
    lights = [{ "pos": (-1, y), "dir":(1, 0) }]
    energy = find_energy(lights)
    if energy > max_energy:
        max_energy = energy

#right->left
for y in range(width):
    energized = set()
    lights = [{ "pos": (width, y), "dir":(-1, 0) }]
    energy = find_energy(lights)
    if energy > max_energy:
        max_energy = energy

print("Part 2:", max_energy)

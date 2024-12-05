manual = set()
folds = []

for line in open("input.data").read().splitlines():
    if line.strip() == "":
        continue

    if line.startswith("fold"):
        line = line.replace("fold along ", "")
        dir, value = line.split("=")
        folds.append((dir, int(value)))
    else:
        x, y = line.split(",")
        manual.add((int(x), int(y)))

WIDTH = max(map(lambda coord: coord[0], manual))
HEIGHT = max(map(lambda coord: coord[1], manual))

first = True
for instruction in folds:
    dir, at = instruction
    if dir == "y":
        HEIGHT = at
        under = set(filter(lambda coord: coord[1] > at, manual))
        manual = set(filter(lambda coord: coord[1] < at, manual))
        for coord in under:
            manual.add((coord[0], at + at - coord[1]))
    elif dir == "x":
        WIDTH = at
        under = set(filter(lambda coord: coord[0] > at, manual))
        manual = set(filter(lambda coord: coord[0] < at, manual))
        for coord in under:
            manual.add((at + at - coord[0], coord[1]))

    if first:
        print("Part 1:", len(manual))
        first = False

def render(on="#", off="."):
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            row.append(on if (x, y) in manual else off)
        print("".join(row))


print("Part 2:")
render(".", " ")

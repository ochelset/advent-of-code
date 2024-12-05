inputdata = open("input.data").read().strip().splitlines()

WIDTH = 50
HEIGHT = 6

def render(screen):
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            row += "#" if screen[(x, y)] == 1 else " "
        print(row)

screen = {}
for y in range(HEIGHT):
    for x in range(WIDTH):
        screen[(x, y)] = 0

for line in inputdata:
    instruction, line = line.split(" ", 1)
    if instruction == "rect":
        w, h = line.split("x")
        for y in range(int(h)):
            for x in range(int(w)):
                screen[(x, y)] = 1
    else:
        target, source, amount = line.replace("x=", "").replace("y=", "").replace("by ", "").split(" ")
        amount = int(amount)

        if target == "column":
            x = int(source)
            column = []
            for y in range(HEIGHT):
                column.append(screen[(x, y)])

            for i in range(amount):
                o = column.pop()
                column.insert(0, o)

            for y in range(HEIGHT):
                screen[(x, y)] = column[y]
        else:
            y = int(source)
            row = []
            for x in range(WIDTH):
                row.append(screen[(x, y)])

            for i in range(amount):
                o = row.pop()
                row.insert(0, o)

            for x in range(WIDTH):
                screen[(x, y)] = row[x]

    #render(screen)
    #input()

print("Part 1:", len(list(filter(lambda x: x == 1, screen.values()))))
print("Part 2:")
render(screen)
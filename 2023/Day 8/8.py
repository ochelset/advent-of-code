data = open("input.data").read().strip().split("\n")

test_data = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".strip().split("\n")

xdata = test_data

inst = data[0]
data = data[2:]

the_map = {}

for line in data:
    key, paths = line.split(" = ")
    paths = paths[1:-1].split(", ")
    the_map[key] = { 'L': paths[0], 'R': paths[1] }

if False:
    i = 0
    pos = 'AAA'

    while pos != 'ZZZ':
        com = inst[i % len(inst)]
        i += 1
        pos = the_map[pos][com]

        #print(pos)
        #input()

    print("Part 1:", i)

i = 0
pos = []
for key in the_map.keys():
    if key[2] == 'A':
        pos.append(key)

finished = False
while not finished:
    com = inst[i % len(inst)]
    i += 1

    finished = True
    new_pos = []
    for p in pos:
        new_pos.append(the_map[p][com])
        if the_map[p][com][2] != 'Z':
            finished = False

    #print(">", pos)
    #print("<", new_pos)
    #input()
    pos = new_pos

print("Part 2:", i)
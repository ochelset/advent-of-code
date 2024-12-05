from itertools import combinations, permutations

data = open("input.data").read().strip().splitlines()
data = """
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
""".strip().splitlines()

valves = {}


def move(current):
    global valves

    valve = valves[current]
    print("@")
    # if valve[0] == 1

    if valve[0] == 0 and not valve[1]:
        for current in valve[2]:
            move(current)


for line in data:
    line = line[6:] \
        .replace("has flow rate=", "") \
        .replace(" tunnel leads to valve ", "") \
        .replace(" tunnels lead to valves ", "")
    source, target = line.split(";")
    valve, rate = source.split(" ")
    targets = target.split(", ")

    valves[valve] = [0, int(rate), targets, 0]  # open/close, rate, targets, flow

# todo, sort by amount of total released pressure per 30 mins for each of them
# todo, start at the first, then find which tunnel leads to the next unopened with the highest rate

pressures = []
for p in permutations(valves.keys()):
    released = 0
    minutes = 30
    p = ["DD", "CC", "BB", "AA", "II", "JJ"]
    pi = None

    # tick, release, move, open
    while minutes:
        minutes -= 1
        input()
        print("== Min %s ==" % (30 - minutes))

        # release
        opened = []
        pressure = 0
        for vv in valves.keys():
            if not valves[vv][0]:
                continue

            opened.append(vv)
            pressure += valves[vv][3]

        if opened:
            print("Valves %s open, releasing" % ", ".join(opened), pressure, "pressure")
            pressures.append(pressure)

        if not opened:
            print("No valves are open")
            if pi is None:
                pi = 0
                print("Move to", p[pi])
                continue

        valve = valves[p[pi]]
        if not valve[0] and valve[1]:
            print("Open", p[pi])
            valve[0] = 1 * valve[1]
            valve[3] = valve[0]
            continue

        pi += 1
        print("Move to", p[pi])

    pressures.add(released)
    # print("POP", released)
print(sorted(pressures))

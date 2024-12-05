from itertools import combinations, permutations

inputdata = """
RT-start
bp-sq
em-bp
end-em
to-MW
to-VK
RT-bp
start-MW
to-hr
sq-AR
RT-hr
bp-to
hr-VK
st-VK
sq-end
MW-sq
to-RT
em-er
bp-hr
MW-em
st-bp
to-start
em-st
st-end
VK-sq
hr-st
""".strip().splitlines()

inputdata = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
""".strip().splitlines()

inputdata = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
""".strip().splitlines()

def visit_cave(cave, path, current):
    path.append(cave)
    if current == "end" or current == "start":
        return

    if len(cave_map[cave]["to"]) == 0:
        print("EMP", cave)
        path.append(current)

    print("W", cave_map[cave]["to"])
    print("+", ",".join(path))
    input()

    for way in cave_map[cave]["to"]:
        if is_lowercase(cave) and "end" not in cave_map[way]["to"]:
            print("IGNRE", way)
            continue
        visit_cave(way, path, cave)

#

def examine(cave, path):
    path.append(cave)
    for way in cave_map[cave]["to"]:
        examine(way, path)

def store(path):
    distinct_paths.add(",".join(path))

def is_lowercase(string) -> bool:
    return string.lower() == string

cave_map = {}
for line in inputdata:
    a, b = line.split("-")
    if a not in cave_map:
        cave_map[a] = { "to": set() }
    if b not in cave_map:
        cave_map[b] = { "to": set() }
    cave_map[a]["to"].add(b)
    cave_map[b]["to"].add(a)

###
###

print(cave_map)
combos = []
input()

def visit(cave, path, visited, level):
    print("visit", cave)
    if cave == "start" and "start" in visited:
        print("Start again")
        return

    if "end" in visited:
        print("End", path)
        return

    path.append(cave)

    current = cave
    if current not in visited:
        visited[current] = 0
    visited[current] += 1
    visited["travel"].append(",".join(path))

    if is_lowercase(cave) and cave not in ["start", "end"]:
        if is_lowercase(path[-2]) and cave_map[cave]["to"] == []:
            visited["travel"].pop()
            path.pop()
            print("dead end", cave, path)
            return

        if not is_lowercase(path[-2]):
            print("GO BACK", path[-2])
            visit(path[-2], path, visited, level)
            return

    print(level*" ", path, current, cave_map[current]["to"], visited)
    input()

    level += 1
    for cave in cave_map[cave]["to"]:
        if is_lowercase(cave) and cave in visited:
            continue
        visit(cave, path, visited, level)
    level -= 1

distinct_paths = set()
travels = {"start": {}}

def check(current, travel):
    for cave in cave_map[current]["to"]:
        travel[cave] = { "paths": []}
        check(cave, travel[cave])


caves = []
s = [i.split("-") for i in inputdata]
for i in s:
    if i[0] not in caves:
        caves.append(i[0])
    if i[1] not in caves:
        caves.append(i[1])

n = len(caves)

def getind(cs):
    for i in range(len(caves)):
        if caves[i] == cs:
            return i

graph = [[0 for j in range(n)] for i in range(n)]
for i in s:
    a = getind(i[0])
    b = getind(i[1])
    graph[a][b] = 1
    graph[b][a] = 1

paths = [[0 for i in range(len(caves))] for i in range(1 << n + 1)]
for i in range(1 << n + 1):
    for j in range(n):
        if i & 1 << j == 0:
            continue

        if not is_lowercase(caves[j]):
            continue

        for k in range(n):
            if is_lowercase(caves[k]):
                continue

            if graph[j][k] == 0:
                continue

            if i & 1 << k == 0:
                continue

            print("+1")
            paths[i][k] += paths[i][j]

print("Part 1:")
print(graph)
for path in paths:
    print(path)


while False:
    size = len(cave_map.keys())
    for i in range(3, (1 << (size + 1))):
        for combo in list(combinations(cave_map.keys(), i)):
            if "start" not in combo or "end" not in combo:
                continue
            print(i, combo)

    break

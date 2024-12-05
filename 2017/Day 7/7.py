data = open("input.data").read().strip().splitlines()
data = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
""".strip().splitlines()

tower = {}


def find_parent(child, t):
    global tower
    for line in data:
        line = line.split(" -> ")
        if len(line) == 1:
            continue

        current, weight = line[0].replace(")", "").split(" (")
        children = line[1].split(", ")

        n = {}
        if child in children:
            n[current] = t
            for kid in children:
                if kid not in n[current]:
                    n[current][kid] = {"w": find_weight(kid)}
                    #n[current][kid]["tw"] = n[current][kid]["w"]
                    #tw += n[current][kid]["w"]
                #print(kid, tw)
            #n[current]["tw"] += tw
            #print("Found!", current, children, n)
            #input(">")
            return find_parent(current, n)
            #tower[current] = children

    #print("<", t)
    return t


def find_weight(child) -> int:
    for line in data:
        if line.startswith(child):
            return int(line.split(")")[0].split("(")[-1])
    return 0


i = 0
while i < len(data):
    line = data[i]
    line = line.split(" -> ")
    current, weight = line[0].replace(")", "").split(" (")
    tower = find_parent(current, tower)
    i += 1
    #input()

print("Part 1:", list(tower.keys())[0])

print(tower["tknk"].keys())

root = list(tower.keys())[0]


def find_balance(start):
    print(">", start)
    for branch in start.keys():
        start[branch]["w"] = find_weight(branch)
        print(branch, start[branch]["w"])
        input()
        find_balance(start[branch])


find_balance(tower[root])
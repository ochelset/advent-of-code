data = open("input.data").read().strip().splitlines()
p1 = 0
p2 = []


def analyze(ptr=[], size=0):
    global tree, p1

    current = tree
    for dir in ptr:
        current = current[dir]

    while data:
        line = data.pop(0)
        if line.startswith("$"):
            parts = line.split(" ")[1:]

            if parts[0] == "cd":
                if parts[1] == "..":
                    ptr.pop()
                    if size < 100000:
                        p1 += size
                    p2.append(size)
                    current["size"] = size
                    return size
                else:
                    ptr.append(parts[1])
                    size += analyze(ptr)
        else:
            parts = line.split(" ")
            if parts[0] == "dir":
                current[parts[1]] = {"type": "dir", "size": 0}
            else:
                current[parts[1]] = {"type": "file", "size": int(parts[0])}
                size += int(parts[0])

    current["size"] = size
    return size


tree = {"/": {"type": "dir"}}
while data:
    size = analyze()

p2.sort()

print("Part 1:", p1)

req = 70000000 - 30000000  # tree["/"]["size"]
used = tree["/"]["size"]
for dir_size in p2:
    if used - dir_size <= req:
        print("Part 2:", dir_size)
        break

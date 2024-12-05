def is_lowercase(string) -> bool:
    return string.lower() == string

def find_paths():
    paths = 0
    unchecked = [{ "name": "start", "path": {"start"}, "visited": None }]
    while unchecked:
        cave = unchecked.pop()
        if cave["name"] == "end":
            paths += 1
            continue

        for path in cave_map[cave["name"]]:
            if path not in cave["path"]:
                new_path = set(cave["path"])
                if is_lowercase(path):
                    new_path.add(path)
                unchecked.append({ "name": path, "path": new_path, "visited": cave["visited"] })
            else:
                if not cave["visited"] and path not in { "start", "end" }:
                    unchecked.append({"name": path, "path": cave["path"], "visited": path })
    return paths

cave_map = {}
for line in open("input.data").read().strip().splitlines():
    a, b = line.split("-")
    if a not in cave_map:
        cave_map[a] = set()
    if b not in cave_map:
        cave_map[b] = set()
    cave_map[a].add(b)
    cave_map[b].add(a)

print("Part 1:", find_paths())
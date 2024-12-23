from collections import deque

data = open("input.data").read().splitlines()

DIRECTIONS = [
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
    (0, 0, -1),
    (0, -1, 0),
    (-1, 0, 0),
]


def add_tuples(a, b):
    return tuple(x + y for x, y in zip(a, b))


def p1(f):
    pieces = set(tuple(map(int, line.split(","))) for line in f)
    ans = len(pieces) * 6
    for p in pieces:
        for d in DIRECTIONS:
            if add_tuples(p, d) in pieces:
                ans -= 1
    return ans


def p2(f):
    pieces = {tuple(map(int, line.split(","))): 0 for line in f}

    min_coords = tuple(min(x) - 1 for x in zip(*pieces))
    max_coords = tuple(max(x) + 1 for x in zip(*pieces))

    start = deque([min_coords])
    visited = set()

    print(min_coords, max_coords)

    while start:
        u = start.pop()
        if u in visited:
            continue
        visited.add(u)

        for d in DIRECTIONS:
            v = add_tuples(u, d)
            if all(a <= b <= c for a, b, c in zip(min_coords, v, max_coords)):
                if v in pieces:
                    pieces[v] += 1
                else:
                    start.append(v)
        print("+", len(start))
    return sum(pieces.values())


print(p1(data))
print(p2(data))

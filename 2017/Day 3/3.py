memory_address = 265149
SPIRAL = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def find_coord_for(target) -> (int, int):
    i = 1
    x = 0
    y = 0
    while True:
        top = i * i
        p = top
        if p == target:
            return x, y

        for w in SPIRAL:
            for n in range(i-1):
                pp = p - n - 1
                x += w[0]
                y += w[1]
                if pp == target:
                    return x, y

            p -= i - 1

        i = i + 2
        x += 1
        y += 1


def find_adjacent_value_for(target) -> int:
    coords = {(0, 0): 1}
    i = 1
    j = 1
    x = 0
    y = 0
    while True:
        for w in SPIRAL:
            for n in range(i - 1):
                j += 1
                x += w[0]
                y += w[1]
                if not (x, y) in coords:
                    value = value_inc_adjacents((x, y), coords)
                    coords[(x, y)] = value

                    if value > target:
                        return value

        i += 2
        x += 1
        y += 1


def distance(a, b) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def value_inc_adjacents(pos, coords) -> int:
    result = 0
    adjacents = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    for adjacent in adjacents:
        pp = (pos[0] + adjacent[0], pos[1] + adjacent[1])
        if pp in coords:
            result += coords[pp]

    return result


pos = find_coord_for(memory_address)
dist = distance(pos, (0, 0))
print("Part 1:", dist)
print("Part 2:", find_adjacent_value_for(memory_address))
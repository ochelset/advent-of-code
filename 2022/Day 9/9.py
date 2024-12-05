data = open("input.data").read().strip().splitlines()

dirs = {
    "U": (0, -1),
    "R": (1, 0),
    "D": (0, 1),
    "L": (-1, 0)
}
tail_pos = set()
tail_pos.add((0, 0))


def is_adjacent(a, b) -> bool:
    if a == b:
        return True

    for pos in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
        t = (a[0] + pos[0], a[1] + pos[1])
        if t == b:
            return True

    return False


def move(rope=[], direction=(0, 0), length=0):
    while length:
        length -= 1
        head = (rope[0][0] + direction[0], rope[0][1] + direction[1])
        rope[0] = head
        prev = head
        for i in range(1, len(rope)):
            knot = rope[i]
            if not is_adjacent(prev, knot):
                catch_up = [prev[0] - knot[0], prev[1] - knot[1]]
                if catch_up[0] == 2:
                    catch_up[0] = 1
                elif catch_up[0] == -2:
                    catch_up[0] = -1
                if catch_up[1] == 2:
                    catch_up[1] = 1
                elif catch_up[1] == -2:
                    catch_up[1] = -1
                catch_up = tuple(catch_up)
                knot = (knot[0] + catch_up[0], knot[1] + catch_up[1])
                rope[i] = knot
            prev = knot

        tail_pos.add(rope[-1])


def get_rope(length=0):
    rope = []
    for i in range(length):
        rope.append((0, 0))
    return rope


def go(length=2):
    global tail_pos
    tail_pos = set()
    rope = get_rope(length)
    for line in data:
        heading, length = line.split(" ")
        move(rope, dirs[heading], int(length))

    return len(tail_pos)


print("Part 1:", go())
print("Part 2:", go(length=10))

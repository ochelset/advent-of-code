lines = open("input.data").read().strip().split("\n")


def get_assigned(rooms_ids: str) -> [int, int]:
    ids = rooms_ids.split("-")
    return int(ids[0]), int(ids[1])


counter = 0
total = 0
for line in lines:
    a, b = line.split(",")
    low_a, high_a = get_assigned(a)
    low_b, high_b = get_assigned(b)

    if (low_a >= low_b and high_a <= high_b) or (low_b >= low_a and high_b <= high_a):
        counter += 1

    #

    overlap = False
    rooms = set()
    for room in range(low_a, high_a+1):
        rooms.add(room)
    for room in range(low_b, high_b+1):
        if room in rooms:
            overlap = True
            break

    if overlap:
        total += 1

print("Part 1:", counter)
print("Part 2:", total)

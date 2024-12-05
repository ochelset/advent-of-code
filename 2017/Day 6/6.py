banks = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
iterations = set()
cycles = []

def spread() -> int:
    cycles.append(str(banks))
    most = max(banks)
    index = banks.index(most)
    banks[index] = 0
    while most > 0:
        index += 1
        if index >= len(banks):
            index = 0
        banks[index] += 1
        most -= 1

    hash = str(banks)
    if hash in iterations:
        return cycles.index(hash)

    iterations.add(hash)
    return 0


steps = 0
while True:
    steps += 1
    cyclus_index = spread()
    if cyclus_index:
        print("Part 1:", steps)
        print("Part 2:", steps - cyclus_index)
        break

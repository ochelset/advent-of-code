import itertools
from functools import lru_cache

#
#

data = open("input.data").read().split("\n")

adapters = [int(n) for n in data]
adapters.sort()

source_joltage = 0
input_joltage = source_joltage
output_joltage = input_joltage
highest_joltage_adapter = max(adapters) + 3

ordered_adapters = [(0, 0)]

while adapters:
    delta = (input_joltage, input_joltage + 3)
    for index, adapter in enumerate(adapters):
        low, high = (abs(adapter-delta[0]), abs(adapter-delta[1]))
        if low+high <= 3:
            ordered_adapters.append((adapter, low))
            input_joltage = adapter
            adapters.pop(index)
            break

ordered_adapters.append((highest_joltage_adapter, 3))

lower = list(filter(lambda x: x[1] == 1, ordered_adapters))
higher = list(filter(lambda x: x[1] == 3, ordered_adapters))

print("Part 1:", len(lower) * (len(higher)))

@lru_cache()
def find_adapters(index: int):
    if index >= len(ordered_adapters):
        return 1

    adapter = ordered_adapters[index]
    counter = find_adapters(index + 1)

    if index + 2 < len(ordered_adapters) and ordered_adapters[index + 2][0] - adapter[0] <= 3:
        counter += find_adapters(index + 2)

        if index + 3 < len(ordered_adapters) and ordered_adapters[index + 3][0] - adapter[0] <= 3:
            counter += find_adapters(index + 3)

    return counter

print("Part 2:", find_adapters(0))

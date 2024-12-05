"""
--- Day 17: No Such Thing as Too Much ---
The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator,
you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters,
there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5

Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?
"""

from itertools import combinations

lines = open("input.data").read().strip().splitlines()


def find_combinations_to_hold(liters: int) -> [int, int]:
    global containers
    combos = set()
    combo_lengths = {}
    for i in range(1, len(containers)):
        for combo in combinations(containers, i):
            combination = []
            filled = 0
            for container in combo:
                if filled < liters:
                    combination.append(str(container[0]) + "." + str(container[1]))
                    filled += container[0]
                if filled == liters:
                    combination.sort()
                    if str(combination) not in combos:
                        if len(combination) not in combo_lengths:
                            combo_lengths[len(combination)] = 0
                        combo_lengths[len(combination)] += 1
                    combos.add(str(combination))
                    break

    minkey = 1000
    for length in combo_lengths.keys():
        if length < minkey:
            minkey = length

    return len(combos), combo_lengths[length]


containers = []
for i in range(len(lines)):
    containers.append((int(lines[i]), i))

l = find_combinations_to_hold(150)
print("Part 1:", l[0])
print("Part 2:", l[1])

"""

"""
from collections import defaultdict

school = list(map(lambda x: int(x), open("input.data").read().split(",")))

def evolve(school: [], days: int) -> int:
    factors = defaultdict(int)
    for fish in school:
        factors[fish] += 1

    for day in range(days):
        for i in range(0, 9):
            factors[i-1] = factors[i]
        factors[8] = factors[-1]
        factors[6] += factors[-1]
        factors[-1] = 0

    return sum(factors.values())

print("Part 1:", evolve(school, days=80))
print("Part 2:", evolve(school, days=256))

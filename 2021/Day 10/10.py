"""

"""
from functools import reduce

inputdata = open("input.data").read().splitlines()

def check(line: str):
    point_table = { ")": 3, "]": 57, "}": 1197, ">": 25137 }
    chunks = []
    for char in line:
        if char in "([{<":
            chunks.append(char)
        else:
            chunk = chunks.pop()
            if char == ")" and chunk != "(":
                return point_table[char]
            elif char == "]" and chunk != "[":
                return point_table[char]
            elif char == "}" and chunk != "{":
                return point_table[char]
            elif char == ">" and chunk != "<":
                return point_table[char]
    return 0

def auto_complete(line: str):
    point_table = { "(": 1, "[": 2, "{": 3, "<": 4 }
    chunks = []
    for char in line:
        if char in "([{<":
            chunks.append(char)
        else:
            chunks.pop()

    score = list(map(lambda chunk: point_table[chunk], chunks))[::-1]
    return reduce(lambda total, point: 5 * total + point, score, 0)

checksums = []
remaining = []

for line in inputdata:
    checksum = check(line)
    checksums.append(checksum)

    if checksum == 0:
        remaining.append(line)

print("Part 1:", sum(checksums))

checksums = []
for line in remaining:
    checksum = auto_complete(line)
    checksums.append(checksum)

checksums = sorted(checksums)

middle = len(checksums) // 2
print("Part 2:", checksums[middle])
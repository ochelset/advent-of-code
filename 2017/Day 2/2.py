from itertools import combinations

spreadsheet = open("input.data").read().strip().replace("\t", " ")

xpreadsheet = """
5 9 2 8
9 4 7 3
3 8 6 5
"""


def diff(row) -> int:
    values = []
    for value in row.split(" "):
        values.append(int(value))

    values.sort()
    return values[-1] - values[0]


def divide(row) -> int:
    values = []
    for value in row.split(" "):
        values.append(int(value))

    output = 0
    for p in combinations(values, 2):
        if p[0] < p[1]:
            p = (p[1], p[0])
        if p[0] % p[1] == 0:
            output += int(p[0] / p[1])
    return output

checksum = 0
for row in spreadsheet.strip().split("\n"):
    checksum += diff(row)

print("Part 1:", checksum)

result = 0
for row in spreadsheet.strip().split("\n"):
    result += divide(row)

print("Part 2:", result)
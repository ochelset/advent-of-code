from collections import deque
import math

test = False
data = open("input.data").read().splitlines()

if test:
    data = """
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122""".strip().splitlines()

VALUES = {
    "0": 0,
    "1": 1,
    "2": 2,
    "-": -1,
    "=": -2
}

VALUES_INVERSE = {
    0: "0",
    1: "1",
    2: "2",
    -1: "-",
    -2: "="
}

def get_snafu(number: str) -> float:
    values = []
    f = 0
    for i, digit in enumerate(number.strip()[::-1]):
        f = 5**i
        values.insert(0, VALUES[digit] * f)
    return sum(values)

def get_snafu_inverse(value: int) -> str:
    result = ""
    while value > 0:
        digit = value % 5
        value = value // 5
        if digit > 2:
            digit -= 5
            value += 1
        result += VALUES_INVERSE[digit]
    return result[::-1]

total = 0
for line in data:
    total += get_snafu(line)

print("Part 1:", get_snafu_inverse(total))


"""

"""

inputdata = open("input.data").read().splitlines()
inputdata = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip().splitlines()

counters = {}
for number in inputdata:
    for i in range(len(number)):
        digit = int(number[i])
        if i not in counters:
            counters[i] = [0,0]
        counters[i][digit] += 1

epsilon = []
gamma = []
for i in range(len(inputdata[0])):
    epsilon.append("1" if counters[i][0] >= counters[i][1] else "0")
    gamma.append("1" if counters[i][0] <= counters[i][1] else "0")

gamma = int("".join(gamma), 2)
epsilon = int("".join(epsilon), 2)

def find_keeper(source: [], pos: int) -> []:
    counters = {}
    for number in source:
        digit = int(number[pos])
        if i not in counters:
            counters[pos] = [0, 0]
        counters[pos][digit] += 1

    return common if counters[i][0] <= counters[i][1] else not_common
    return common if counters[pos][0] <= counters[i][1] else not_common


def find_rating(common: str) -> int:
    not_common = "0" if common == "1" else "1"
    source = inputdata[:]
    remainders = []
    while len(remainders) != 1:
        print("a")
        for i in range(len(source[0])):
            print("b")

            keeper = find_keeper(source, i)
            remainders = list(filter(lambda x: x[i] == keeper, source))

            if len(remainders) == 1:
                break

            source = remainders[:]
            remainders = []

    return int(remainders[0], 2)

oxygen = find_rating("1")
co2 = find_rating("0")

print("Part 1:", epsilon * gamma)
print("Part 2:", oxygen * co2)



#print("Part 2:")
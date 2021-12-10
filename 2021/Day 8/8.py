"""

"""
from itertools import permutations

inputdata = open("input.data").read().splitlines()

uniques = { 2: 1, 3: 7, 4: 4, 7: 8 }
counter = 0

def store(signal: str, value: int, signal_map: {}):
    combos = list(permutations(signal))
    for combo in combos:
        signal_map["".join(combo)] = value

def remove(value, values):
    return list(filter(lambda x: x != value, values))

def overlapping(a, b) -> bool:
    for letter in a:
        if letter not in b:
            return False
    return True

def parse_signal(input: [], output: []) -> int:
    signal_map = {}
    inverse = {}

    found = []
    missing = []
    for value in input:
        if len(value) in uniques:
            signals[value] = uniques[len(value)]

        if len(value) == 2:
            inverse[value] = 1
        elif len(value) == 4:
            inverse[value] = 4
        elif len(value) == 3:
            inverse[value] = 7
        elif len(value) == 7:
            inverse[value] = 8

        if value in inverse:
            found.append((inverse[value], value))
            store(value, inverse[value], signal_map)
        else:
            missing.append(value)

    six_possibles = [0, 6, 9]
    five_possibles = [2, 3, 5]
    while len(missing):
        for value in missing:
            if len(value) == 6:
                possibles = six_possibles[:]
                if len(possibles) > 1:
                    for key, number in inverse.items():
                        if number == 0 and overlapping(key, value):
                            possibles = remove(6, possibles)
                            possibles = remove(9, possibles)
                        elif number == 1 and overlapping(key, value):
                            possibles = remove(6, possibles)
                        elif number == 3 and overlapping(key, value):
                            possibles = remove(0, possibles)
                            possibles = remove(6, possibles)
                        elif number == 4 and overlapping(key, value):
                            possibles = remove(0, possibles)
                        elif number == 5 and overlapping(key, value):
                            possibles = remove(0, possibles)

                if len(possibles) == 1:
                    number = possibles.pop()
                    six_possibles = remove(number, six_possibles)
                    found.append((number, value))
                    inverse[value] = number
                    store(value, number, signal_map)
                    missing = remove(value, missing)
                    break

            elif len(value) == 5:
                possibles = five_possibles[:]
                if len(possibles) > 1:
                    for key, number in inverse.items():
                        if number == 1 and overlapping(key, value):
                            possibles = remove(2, possibles)
                            possibles = remove(5, possibles)
                        if number == 6 and overlapping(value, key):
                            possibles = remove(2, possibles)
                            possibles = remove(3, possibles)
                        if number == 9 and overlapping(key, value):
                            possibles = remove(3, possibles)

                if len(possibles) == 1:
                    number = possibles.pop()
                    five_possibles = remove(number, five_possibles)
                    found.append((number, value))
                    inverse[value] = number
                    store(value, number, signal_map)
                    missing = remove(value, missing)
                    break

    result = []
    for value in output:
        result.append(str(signal_map[value]))

    return(int("".join(result)))


total = 0
for line in inputdata:
    signals = {}
    signal, output = line.split(" | ")
    signal = signal.split(" ")
    output = output.split(" ")

    for values in output:
        if len(values) in uniques:
            counter += 1
            signals[values] = uniques[len(values)]

    display = parse_signal(signal, output)
    total += display

print("Part 1:", counter)
print("Part 2:", total)

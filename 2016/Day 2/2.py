data = open("input.data").read().strip().splitlines()

numpad = [
    "00000",
    "01230",
    "04560",
    "07890",
    "00000"
]

keypad = [
    "0000000",
    "0001000",
    "0023400",
    "0567890",
    "00ABC00",
    "000D000",
    "0000000"
]


def key(pos, pad):
    return pad[pos[1]][pos[0]]

def hack(data, pad, last_key=(2, 2)):
    code = []

    for line in data:
        for ins in line:
            next_key = last_key

            if ins == "U":
                next_key = (last_key[0], last_key[1]-1)
            elif ins == "D":
                next_key = (last_key[0], last_key[1]+1)
            elif ins == "L":
                next_key = (last_key[0]-1, last_key[1])
            elif ins == "R":
                next_key = (last_key[0]+1, last_key[1])

            if key(next_key, pad) == "0":
                continue

            last_key = next_key

        code.append(str(key(last_key, pad)))

    return "".join(code)

print("Part 1:", hack(data, numpad))
print("Part 2:", hack(data, keypad, (1, 3)))
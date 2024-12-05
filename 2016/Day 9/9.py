inputdata = open("input.data").read().strip()

def decompress(data, v2=False) -> int:
    i = 0
    length = 0
    while i < len(data):
        char = data[i]
        if char == "(":
            start = i + 1
            while True:
                if data[i] == ")":
                    break
                i += 1

            nums, repeat = (int(x) for x in data[start:i].split("x"))
            block = data[i+1 : i+nums+1]

            if v2 and "(" in block:
                length += decompress(block, v2) * repeat
            else:
                length += nums * repeat

            i += nums + 1
        else:
            length += 1
            i += 1

    return length

print("Part 1:", decompress(inputdata))
print("Part 2:", decompress(inputdata, v2=True))
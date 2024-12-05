lines = open("input.data").read().strip().split("\n")


def priority(char) -> int:
    value = ord(char) - 64
    if value > 26:
        value = ord(char) - 96
    else:
        value += 26
    return value


items = []
for line in lines:
    a = line[:int(len(line) / 2)]
    b = line.replace(a, "")
    for item in set(a).intersection(set(b)):
        items.append(priority(item))

print("Part 1:", sum(items))

badges = []
for i in range(0, len(lines), 3):
    a, b, c = lines[i:i+3]
    for char in set(a).intersection(set(b)).intersection(set(c)):
        badges.append(priority(char))

print("Part 2:", sum(badges))
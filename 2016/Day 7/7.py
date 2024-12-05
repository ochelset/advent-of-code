inputdata = open("input.data").read().strip().splitlines()

answer1 = 0
for line in inputdata:
    valid = False
    inside = False

    i = 2
    while True:
        ab = line[i-2:i]
        ba = line[i:i+2][::-1]
        if len(ab) < 2 or len(ba) < 2:
            break

        if not inside and ab == ba:
            valid = ab[0] != ab[1]
        if inside and ab == ba:
            valid = False
            break

        i += 1
        if "[" in ba or "]" in ba:
            inside = not inside
            i += 1

    if valid:
        answer1 += 1

answer2 = 0
for line in inputdata:
    hypernet = False
    outside = set()
    inside = set()

    i = 3
    while True:
        aba = line[i-3:i]
        if len(aba) < 3:
            break

        i += 1
        if "[" in aba or "]" in aba:
            hypernet = not hypernet
            continue

        if aba[0] == aba[2] and aba[0] != aba[1]:
            if hypernet:
                inside.add(aba[1] + aba[0] + aba[1])
            else:
                outside.add(aba)

    if len(inside.intersection(outside)) != 0:
        answer2 += 1

print("Part 1:", answer1)
print("Part 2:", answer2)
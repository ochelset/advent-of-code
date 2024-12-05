lines = open("input.data").read().strip().split("\n")

cals = []
elf = 0
n = 0

while lines:
    line = lines.pop()
    if line.strip() == "":
        cals.append(elf)
        elf = 0
        n += 1
        continue

    calories = int(line)
    elf += calories

print("Part 1:", max(cals), "calories")
print("Part 2:", sum(sorted(cals)[-3::]), "calories")
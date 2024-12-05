data = open("input.data").read()
stacks = {}
crates, instructions = data.split("\n\n")


def move(amount, source, target, locked=False):
    if not locked:
        for i in range(amount):
            stacks[target][:0] = stacks[source].pop(0)
    else:
        new_stack = stacks[source][0:amount]
        for i in range(amount):
            if len(stacks[source]):
                stacks[source].pop(0)
        for j in stacks[target]:
            new_stack.append(j)
        stacks[target] = new_stack


def arrange(locked=False) -> str:
    global stacks
    stacks = {}
    for line in crates.splitlines():
        if line.startswith(" 1"):
            break

        for i in range(0, len(line), 4):
            stack = int(i / 4) + 1
            if stack not in stacks:
                stacks[stack] = []

            crate = line[i:i+4].strip().replace("[", "").replace("]", "")
            if crate == "":
                continue

            stacks[stack].append(crate)

    for instruction in instructions.splitlines():
        instruction = instruction.replace("move ", "").replace("from ", "").replace("to ", "")
        amount, source, target = instruction.split(" ")
        move(int(amount), int(source), int(target), locked)

    name = ""
    for i in range(len(stacks.keys())):
        name += stacks[i+1][0]

    return name

print("Part 1:", arrange())
print("Part 2:", arrange(True))
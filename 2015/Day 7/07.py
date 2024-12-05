instructions = open("input.data").read().strip().split("\n")
circuit = {}


def ensure_16_bit(value) -> int:
    return value & 0xffff


def get_line_for(source: str) -> str or None:
    for l in instructions:
        if l.endswith(" -> " + source):
            return l
    return None


def add_from(line: str):
    if not line:
        return

    command, wire = line.split(" -> ")
    if wire in circuit:
        return

    circuit[wire] = 0

    if command.isdigit():
        circuit[wire] = int(command)
    elif command.startswith("NOT "):
        source = command.replace("NOT ", "")
        add_from(get_line_for(source))
        circuit[wire] = ensure_16_bit(~circuit[source])
    elif len(command.split(" ")) == 1:
        add_from(get_line_for(command))
        circuit[wire] = circuit[command]
    else:
        a, command, b = command.split(" ")
        if a.isdigit() and not b.isdigit():
            c = a
            a = b
            b = c

        if not a.isdigit():
            add_from(get_line_for(a))
            a = circuit[a]
        else:
            a = int(a)

        if not b.isdigit():
            add_from(get_line_for(b))
            b = circuit[b]
        else:
            b = int(b)

        if command == "AND":
            circuit[wire] = ensure_16_bit(a & b)
        if command == "OR":
            circuit[wire] = ensure_16_bit(a | b)
        if command == "LSHIFT":
            circuit[wire] = ensure_16_bit(a << b)
        if command == "RSHIFT":
            circuit[wire] = ensure_16_bit(a >> b)


while len(instructions):
    add_from(instructions.pop())

print("Part 1:", circuit["a"])

circuit = {"b": circuit["a"]}

instructions = open("input.data").read().strip().split("\n")
while len(instructions):
    add_from(instructions.pop())

print("Part 2:", circuit["a"])

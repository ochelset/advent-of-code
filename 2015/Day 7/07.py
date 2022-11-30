instructionsx = """
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
""".strip().split("\n")

circuit = {}
instructions = open("input.data").read().strip().split("\n")

def ensure_16_bit(value) -> int:
    return value & 0xffff


def get_line_for(source: str) -> str:
    for l in instructions:
        if l.endswith(" -> " + source):
            return l
    return None

def addFrom(line: str):
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
        addFrom(get_line_for(source))
        circuit[wire] = ensure_16_bit(~circuit[source])
    elif len(command.split(" ")) == 1:
        addFrom(get_line_for(command))
        circuit[wire] = circuit[command]
    else:
        a, command, b = command.split(" ")
        if a.isdigit() and not b.isdigit():
            c = a
            a = b
            b = c

        if not a.isdigit():
            addFrom(get_line_for(a))
            a = circuit[a]
        else:
            a = int(a)

        if not b.isdigit():
            addFrom(get_line_for(b))
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

instructions = open("input.data").read().strip().split("\n")

while len(instructions):
    addFrom(instructions.pop())

print("Part 1:", circuit["a"])

circuit = { "b": circuit["a"] }

instructions = open("input.data").read().strip().split("\n")
while len(instructions):
    addFrom(instructions.pop())

print("Part 2:", circuit["a"])

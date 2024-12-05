data = open("input.data").read().strip().splitlines()

datax = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
""".strip().splitlines()


def apply(amount, source, op, value, line) -> int:
    result = 0
    if op == ">":
        if source > value:
            result = amount
    elif op == "<":
        if source < value:
            result = amount
    elif op == "<=":
        if source <= value:
            result = amount
    elif op == ">=":
        if source >= value:
            result = amount
    elif op == "==":
        if source == value:
            result = amount
    elif op == "!=":
        if source != value:
            result = amount
    else:
        print(repr(op), line)
        print(source, op, value)
        x = 1 / 0

    return result


mem = {}
max_value = 0
for line in data:
    target, command, amount, condition, source, op, value = line.split(" ")
    amount = int(amount)
    value = int(value)

    # print(target, command, amount, condition, source, op, value)
    if target not in mem:
        mem[target] = 0
    if source not in mem:
        mem[source] = 0

    if command == "inc":
        mem[target] += apply(amount, mem[source], op, value, line)
    if command == "dec":
        mem[target] -= apply(amount, mem[source], op, value, line)

    max_value = max(max_value, mem[target])
    # print(target, mem[target])
    # input()

registers = []
for key in mem.keys():
    registers.append(mem[key])

print("Part 1:", max(registers))
print("Part 2:", max_value)

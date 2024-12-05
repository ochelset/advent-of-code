data = open("input.data").read().strip()
data1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
data2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def run(data, p2=False):
    index = 0
    instructions = []
    enabled = True
    while index < len(data):
        memory = data[index:]

        if p2:
            if memory.startswith("do()"):
                enabled = True
                index = index + 4
                continue

            if memory.startswith("don't()"):
                enabled = False
                index = index + 7
                continue

        if not memory.startswith("mul("):
            index = index + 1
            continue

        instruction = memory[:4]
        index += 4

        valid = True
        while True:
            char = data[index]
            index += 1

            if char in " ,0123456789)":
                instruction += char
            else:
                valid = False
                break
            if char == ")":
                break

        # print(instruction, valid, enabled)
        if valid and enabled:
            instructions.append(instruction)

    result = 0
    for instruction in instructions:
        a, b = [int(x) for x in instruction[4:-1].split(",")]
        # print(a, b)
        result += a * b

    return result


print("Part 1:", run(data))
print("Part 2:", run(data, True))

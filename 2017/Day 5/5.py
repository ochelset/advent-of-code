data = open("input.data").read().strip().split("\n")

test_data = """
0
3
0
1
-3
""".strip().split("\n")

instructions = []
for instruction in data:
    instructions.append(int(instruction))


def play(instructions=[], phase=0) -> int:
    pointer = 0
    steps = 0
    while True:
        if pointer >= len(instructions):
            return steps

        instruction = instructions[pointer]
        step = 1
        if phase == 1 and instruction >= 3:
            step = -1
        prev_pointer = pointer
        pointer += instruction
        instructions[prev_pointer] += step
        steps += 1

print("Part 1:", play(instructions[::]))
print("Part 2:", play(instructions[::], 1))


inputdata = open("input.data").read().strip().splitlines()

inputdatax = """
inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2
""".strip().splitlines()

memory = {
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0
}

model_number = []
index = 11111111111111
index = 99999999999999

while True:
    if index > 99999999999999:
        print("BREAK ON MAX")
        break

    if "0" in str(index):
        index -= 1
        continue

    inp = str(index).ljust(14, "0")
    inp_index = 0

    memory["w"] = 0
    memory["x"] = 0
    memory["y"] = 0
    memory["z"] = 0

    for line in inputdata:
        line = line.split(" ")

        if len(line) < 3:
            line.append("")

        instruction = line[0]
        if instruction == "inp":
            memory[line[1]] = int(inp[inp_index])
            inp_index += 1

        elif instruction == "add":
            m = memory[line[2]] if line[2] in memory else int(line[2])
            memory[line[1]] += m

        elif instruction == "mul":
            m = memory[line[2]] if line[2] in memory else int(line[2])
            memory[line[1]] *= m

        elif instruction == "div":
            m = memory[line[2]] if line[2] in memory else int(line[2])
            memory[line[1]] //= m

        elif instruction == "mod":
            m = memory[line[2]] if line[2] in memory else int(line[2])
            memory[line[1]] %= m

        elif instruction == "eql":
            m = memory[line[2]] if line[2] in memory else int(line[2])
            memory[line[1]] = 1 if memory[line[1]] == m else 0

    if memory["z"] == 0:
        print(index, "VALID")
        print(memory)
        input()

    index -= 1

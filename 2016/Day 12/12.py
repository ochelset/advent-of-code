inputdata = open("input.data").read().strip().splitlines()

def run(memory: {}):
    cpu_pointer = 0
    while cpu_pointer < len(inputdata):
        instr = inputdata[cpu_pointer].split(" ")

        if len(instr) == 3:
            value = instr[1]
            if value.isdigit():
                value = int(value)
            else:
                if value not in memory:
                    memory[value] = 0
                value = memory[value]

            if instr[0] == "cpy":
                memory[instr[2]] = value
            if instr[0] == "jnz" and value != 0:
                cpu_pointer += int(instr[2])
                continue

        elif len(instr) == 2:
            if instr[0] == "inc":
                memory[instr[1]] += 1
            elif instr[0] == "dec":
                memory[instr[1]] -= 1

        cpu_pointer += 1

memory = {}
for i in range(2):
    run(memory)
    print("Part %s:" % (i+1), memory["a"])
    memory = { "c": 1 }

data = open("input.data").read().strip().split("\n")

def get_instruction(command: str) -> tuple:
    return tuple(command.split(" = "))

def convert_value_to_36bit(value: int) -> str:
    output = bin(value)[2:]
    return output.rjust(36, "0")

def apply_mask_to_value(value: str, mask: str) -> str:
    output = []
    for index, bit in enumerate(mask):
        if bit == "X":
            output.append(value[index])
        else:
            output.append(bit)

    return "".join(output)

def get_address_mask(address: str, mask: str) -> str:
    output = []
    for index, bit in enumerate(mask):
        if bit == "0":
            output.append(address[index])
        elif bit == "1":
            output.append("1")
        else:
            output.append(bit)

    return "".join(output)

def write_to_memory(memory: dict, address: str, value: int):
    incrementors = []
    simplified = []
    for index, bit in enumerate(address):
        if bit == "X":
            incrementors.append(index)
            simplified.append("1")
    simplified = "".join(simplified)

    for n in range(int(simplified, 2) + 1):
        counter = bin(n)[2:].rjust(len(simplified), "0")
        float_address = [n for n in address]
        for index, incrementor in enumerate(incrementors):
            float_address[incrementor] = counter[index]

        float_address = "".join(float_address)
        memory[int(float_address, 2)] = value


def part1(data: list):
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    memory = {}

    for line in data:
        instruction, value = get_instruction(line)
        if instruction == "mask":
            mask = value
            continue

        address = int(instruction[4:-1])
        converted_value = convert_value_to_36bit(int(value))
        masked_value = apply_mask_to_value(converted_value, mask)
        value = int(masked_value, 2)

        memory[address] = value

    result = 0
    for k in memory.keys():
        result += memory[k]

    print("Part 1:", result)

def part2(data: list):
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    memory = {}

    for line in data:
        instruction, value = get_instruction(line)
        if instruction == "mask":
            mask = value
            continue

        value = int(value)
        address = int(instruction[4:-1])
        converted_address = convert_value_to_36bit(address)
        address_mask = get_address_mask(converted_address, mask)

        write_to_memory(memory, address_mask, value)

    result = 0
    for k in memory.keys():
        result += memory[k]

    print("Part 2:", result)

part1(data)
part2(data)

data = open("input.data").read().strip()


def cancel_chars():
    global data

    new_data = []
    skip = False
    for char in data:
        if skip:
            skip = False
            continue
        if char == "!":
            skip = True
            continue
        new_data.append(char)
    data = "".join(new_data)


def remove_garbage():
    global data

    new_data = []
    garbage = False
    removed = 0
    for char in data:
        if char == "<" and not garbage:
            garbage = True
            continue
        if char == ">":
            garbage = False
            continue
        if garbage:
            removed += 1
            continue
        new_data.append(char)

    print("Part 2:", removed)
    data = "".join(new_data)


def parse_stream():
    level = 0
    points = 0
    for char in data:
        if char == "{":
            level += 1
            points += level
        if char == "}":
            level -= 1

    return points


def find_block_end():
    i = 0
    while True:
        if data[i] == "}":
            return i + 1
        i += 1


cancel_chars()
remove_garbage()
score = parse_stream()

print("Part 1:", score)

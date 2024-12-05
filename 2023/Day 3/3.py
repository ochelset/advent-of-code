data = open("input.data").read().strip().split("\n")

test_data = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip().split("\n")

sdata = test_data

result_1 = 0

nums = []
symbols = []

s = ''
for y in range(len(data)):
    for x in range(len(data[0])):
        char = data[y][x]
        if char == ".":
            if s != '':
                nums.append({ "value": int(s), "x": x-len(s), "y": y, "x2": x-1, "valid": False })
                s = ''
        elif char.isdigit():
            s += char
        else:
            if s != '':
                nums.append({ "value": int(s), "x": x-len(s), "y": y, "x2": x-1, "valid": False })
                s = ''
            symbols.append((x, y, char))
    if s != '':
        nums.append({ "value": int(s), "x": x-len(s), "y": y, "x2": x-1, "valid": False })
        s = ''


#print(nums)
gear_ratio = 0

for symbol in symbols:
    #print("SYM", symbol)
    adjacents = set()
    for num in nums:
        if num["valid"] == True:
            continue

        for neighbor in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
            pos = (symbol[0] + neighbor[0], symbol[1] + neighbor[1])
            #if pos == (2, 0):
            #    print("??", num, nums[num]["y"] == pos[1])

            if num["y"] == pos[1] and pos[0] >= num["x"] and pos[0] <= num["x2"]:
                num["valid"] = True
                adjacents.add(num["value"])
                #print(pos)
                #break

    #print(adjacents)
    if symbol[2] == '*' and len(adjacents) == 2:
        adjacents = list(adjacents)
        gear_ratio += adjacents[0] * adjacents[1]
        #print("gear", adjacents, adjacents[0] * adjacents[1])

for num in nums:
    if num["valid"]:
        result_1 += num["value"]

print("Part 1:", result_1)
print("Part 2:", gear_ratio)

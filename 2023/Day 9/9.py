data = open("input.data").read().strip().split("\n")

test_data = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip().split("\n")

xdata = test_data

result = 0
for line in data:
    rows = [[int(x) for x in line.split(" ")]]

    while True:
        row = rows[-1]
        next_row = []
        sum = 0
        for i, number in enumerate(row):
            if i > 0:
                diff = number - row[i-1]
                next_row.append(diff)
                sum += diff

        if sum == 0:
            next_row.append(0)
            rows.append(next_row)
            diff = rows[-1][-1] + rows[-2][-1]

            #print("Row X", rows[-1], diff)
            for y in range(len(rows)-2, -1, -1):
                diff = rows[y+1][-1] + rows[y][-1]
                rows[y].append(diff)
            result += rows[0][-1]
            break
        else:
            rows.append(next_row)

print("Part 1:", result)

result = 0
for line in data:
    rows = [[int(x) for x in line.split(" ")]]

    while True:
        row = rows[-1]
        next_row = []
        sum = 0
        for i, number in enumerate(row):
            if i > 0:
                diff = number - row[i-1]
                next_row.append(diff)
                sum += diff

        if sum == 0:
            next_row.insert(0, 0)
            rows.append(next_row)
            diff = rows[-1][0] - rows[-2][0]

            print("Row", rows[-1])
            for y in range(len(rows)-2, -1, -1):
                diff = rows[y][0] - rows[y+1][0]
                rows[y].insert(0, diff)
                print("Row", rows[y])
            result += rows[0][0]
            break
        else:
            rows.append(next_row)

print("Part 2:", result)
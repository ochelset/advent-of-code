testdata = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
""".strip().split("\n\n")

testdata2 = """
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
""".strip().split("\n\n")

data = open("input.data").read().strip().split("\n\n")

def is_ticket_valid(ticket: list, groups: list) -> list:
    #print("VALIDATE", ticket)
    valid = True
    invalid_numbers = []
    for number in ticket:
        valid_group = False
        for group in groups:
            for range_set in group:
                #print("G", range)
                if number >= range_set[0] and number <= range_set[1]:
                    #print("Valid", number)
                    valid_group = True
                    break

            #print(">", number, group, valid_group)

            if valid_group:
                break

        if not valid_group:
            invalid_numbers.append(number)

        valid = valid and valid_group

    return invalid_numbers

def in_group(number: int, group: list) -> int:
    result = 0
    if number >= group[0][0] and number <= group[0][1]:
        result = 1
    if number >= group[1][0] and number <= group[1][1]:
       result = 1

    return result

definitions = {}

def find_group_for(column: int, numbers: list, groups: list):
    output = []
    valid_group = True
    column_name = ''

    #print("Len num:", len(numbers))
    #print("Len grp:", len(groups))
    possibles = []
    if not possibles:
        for n in range(2):
            possibles.append((len(groups)) * [0])

        for ruleset_index, ruleset in enumerate(groups):
            possibles[0][ruleset_index] = ruleset[0][2]

    print()
    print("--------------------")
    print("RANG", groups)
    print("NUMS", numbers)

    for row, number in enumerate(numbers):
        print("ROW", row, number)
        input()
        for col, group in enumerate(groups):
            print("X:", col, number, group, in_group(number, group))
            possibles[1][col] += in_group(number, group)

    print("POSS", possibles)
    for i, row in enumerate(possibles):
        print(">", row)
    print()

    group_id = (0, 0, 0, 0)
    for i, col in enumerate(possibles[1]):
        if col > group_id[0]:
            group_id = (col, i, column, possibles[0][i])

    print("?", possibles)
    print("=", group_id)
    input()

    return group_id

def part1(data: list):
    ranges = []

    rules = data[0].split("\n")
    for rule in rules:
        identificator, rule = rule.split(": ", 1)
        rule_ranges = rule.split(" or ")
        range_group = []
        for range in rule_ranges:
            low, high = range.split("-")
            range_group.append((int(low), int(high)))
        ranges.append(range_group)

    error_rate = [0]
    for ticket_data in data[2].split("\n")[1:]:
        ticket = [int(n) for n in ticket_data.split(",")]
        errors = is_ticket_valid(ticket, ranges)
        error_rate.extend(errors)

    print("Part 1:", sum(error_rate))

def part2(data: list):
    my_ticket = [int(n) for n in data[1].split("\n")[1].split(",")]
    ranges = []
    rules = data[0].split("\n")

    for rule in rules:
        identificator, rule = rule.split(": ", 1)
        rule_ranges = rule.split(" or ")
        range_group = []
        for rule_range in rule_ranges:
            low, high = rule_range.split("-")
            range_group.append((int(low), int(high), identificator))
        ranges.append(range_group)

    valid_tickets = []
    for ticket_data in data[2].split("\n")[1:]:
        ticket = [int(n) for n in ticket_data.split(",")]
        error = is_ticket_valid(ticket, ranges)
        if not error:
            valid_tickets.append(ticket)

    #
    memory = set()
    print("VALID", valid_tickets)
    print("RANGES", ranges)

    #for ticket in valid_tickets:
    #    for i, number in enumerate(ticket):
    #        print(">", i, number)

    order = []
    #for i in range(len(my_ticket)):
    #    column = list(map(lambda x: x[i], valid_tickets))
    #    group = find_group_for(i, column, ranges)
    #    print("<---", i, group, column)
    #    order.append(ranges.pop(group[1])[0][2])
    #    #print("====", group[2], ranges)

    possibles = {}
    identificators = set([x[0][2] for x in ranges])

    while True:
        for group in ranges:
            low = set(range(group[0][0], group[0][1]+1))
            low.update(range(group[1][0], group[1][1]+1))
            possibles[group[0][2]] = set(range(len(my_ticket)))
            #high = set(range(group[1][0], group[1][1]+1))
            print("Group", group[0][2], low)
            for i in range(len(my_ticket)):
                column = list(map(lambda x: x[i], valid_tickets))
                print(i, column, set(column).difference(low))
                if set(column).difference(low):
                    possibles[group[0][2]].discard(i)
                    print("Column", i, "can't be", group[0][2])

            #print("T", ticket)
                #for col, number in enumerate(ticket):
                #    if number not in low:
                #        possibles[col].discard(group[0][2])
                #        print("Column", col, "can't be", group[0][2])
                #    #print(col, number, number in low)
        print("P", possibles)
        input()

    print(order)
    print(my_ticket)
    result = 1
    for index, key in enumerate(order):
        if key.startswith("departure"):
            print(index, key, my_ticket[index])
            result *= my_ticket[index]

    print("Part 2:", result)

part1(data)
print("***\n")
part2(testdata2)
#part2(data)

"""
2478056818961 is wrong (too high!!!)
"""
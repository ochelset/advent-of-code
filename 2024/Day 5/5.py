data = open("input.data").read().strip().split("\n\n")
datax = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".strip().split("\n\n")

rules = []
for line in data[0].splitlines():
    a, b = line.split("|")
    rules.append((int(a), int(b)))

updates = []
for line in data[1].splitlines():
    updates.append([int(x) for x in line.split(",")])


def get_rules(page: int) -> [int]:
    return [x for x in rules if x[0] == page]


def is_valid(update: [int]) -> bool:
    index = 0
    valid = True
    while valid and index < len(update):
        page = update[index]
        page_rules = get_rules(page)
        for rule in page_rules:
            try:
                p1_index = update.index(rule[0])
                p2_index = update.index(rule[1])
                if p1_index > p2_index:
                    valid = False
            except:
                pass

        index += 1

        if not valid:
            break

    return valid


valid_updates = []
invalid_updates = []
for update in updates:
    if is_valid(update):
        valid_updates.append(update)
    else:
        invalid_updates.append(update)

result = 0
for update in valid_updates:
    middle = len(update) // 2
    result += update[middle]

print("Part 1:", result)

number = 0
valid_updates = []
for update in invalid_updates:
    number += 1
    reordered_update = []

    index = 0
    while index < len(update):
        page = update[index]
        page_rules = get_rules(page)

        applied = False
        insert_at = len(reordered_update) + 1
        possible_inserts = []
        for rule in page_rules:
            try:
                p1_index = reordered_update.index(rule[0])
            except:
                p1_index = -1

            try:
                p2_index = reordered_update.index(rule[1])
            except:
                p2_index = -1

            if p1_index == -1 and p2_index != -1:
                possible_inserts.append(p2_index)

        if len(possible_inserts) > 0:
            insert_at = min(possible_inserts)

        reordered_update.insert(insert_at, page)
        index += 1

    valid_updates.append(reordered_update)

result = 0
for update in valid_updates:
    middle = len(update) // 2
    result += update[middle]

print("Part 2:", result)

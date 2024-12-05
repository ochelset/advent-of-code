testdata = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
""".strip().replace('"', "").split("\n\n")

rules = {}

def parse_rules(data: str):
    global rules
    for line in data.split("\n"):
        num, rule = line.split(": ")
        if rule in ("a", "b"):
            rules[num] = rule
        elif rule.find("|") != -1:
            rules[num] = { "rule": [n.split(" ") for n in rule.split(" | ")] }
        else:
            rules[num] = { "rule": [rule.split(" ")]}

    for key in rules.keys():
        if "rule" in rules[key]:
            print("> KEY", key, rules[key]["rule"])
            for index, rule in enumerate(rules[key]["rule"]):
                for child_num in rule:
                    next_level = rules[child_num]
                    if next_level in ("a", "b"):
                        rules[key][child_num] = next_level
                    else:
                        rules[key][child_num] = next_level

                print("RULE", index, rule)
        else:
            print("> KEY", key, "<", rules[key])

    print()
    print(">>", rules)
    for key in rules.keys():
        print(">>", key, rules[key])


def get_rules_for(index: str) -> list:
    global rules
    ruleset = []

    for rule in rules[index].split(" "):
        if rule in rules:
            rule = rules[rule]
        if rule.find(" ") != -1:
            print("?", rule)
        ruleset.append(rule)

    return ruleset

def is_valid_message(message: str) -> bool:
    global rules
    ruleset = rules["0"]
    print(ruleset)
    for index, char in enumerate(message):
        valid_char = is_char_valid(char, )
    return True


def part1(data: list):
    global rules
    parse_rules(data[0])
    #ruleset = get_rules_for("0")
    #print(ruleset)

    for message in data[1].split("\n"):
        print(message, is_valid_message(message))




part1(testdata)
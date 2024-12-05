import itertools
from collections import Counter

data = open("input.data").read().strip().split("\n\n")

test_data = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
""".strip().split("\n\n")

#data = test_data
workflows = { "A": [], "R": [] }
ratings = []

for workflow in data[0].split("\n"):
    name, rule = workflow[:-1].split("{")
    workflows[name] = { "rule": rule }

for rating in data[1].split("\n"):
    xmas = rating[1:-1].split(",")
    rating = { }
    for part in xmas:
        name, value = part.split("=")
        rating[name] = int(value)
    ratings.append(rating)

for rating in ratings:
    workflow = workflows["in"]
    #print("-"*80)
    #print("Rating:", rating)

    rule = workflow["rule"]
    while True:
        #print("Rule:", rule)
        reg = rule[0]
        op = rule[1]
        index = rule.find(":")
        value = int(rule[2:index])

        #print(rating[reg], op, value)
        valid = False
        if op == "<":
            valid = rating[reg] < value
        elif op == ">":
            valid = rating[reg] > value
        else:
            print("INVALID RULE", op)

        rule = rule[index+1:]
        next_gt = rule.find(">")
        next_lt = rule.find("<")
        next_rule_index = -1
        if next_gt == -1 and next_lt != -1:
            next_rule_index = next_lt
        if next_lt == -1 and next_gt != -1:
            next_rule_index = next_gt
        if next_lt != -1 and next_gt != -1:
            next_rule_index = min(next_lt, next_gt)

        target = None
        if next_rule_index == -1:
            #print("SPLIT", rule, next_gt, next_lt)
            remain = rule.split(",")
        else:
            #print("??", rule)
            remain = rule[:next_rule_index-1].split(",")
            rule = rule[next_rule_index-1:]
            target = remain[not valid]
            #print("REM", next_rule_index, remain, valid, rule, "->", target)

        target = remain[not valid]
        #print("GOTO", target, valid, rule)
        if target == "A":
            #print("-> A")
            workflows["A"].append(rating)
            break
        if target == "R":
            #print("-> R")
            workflows["R"].append(rating)
            break

        if target in workflows:
            #print("->", target)
            workflow = workflows[target]
            rule = workflow["rule"]
        #else:
        #    print("XXX", target)
        #    print("REM", next_rule_index, remain, valid, rule, "-> TARGET:", target)
        #    input()

        #input()

result = 0
for rating in workflows["A"]:
    result += rating["x"] + rating["m"] + rating["a"] + rating["s"]

print("Part 1:", result)
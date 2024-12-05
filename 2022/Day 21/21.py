data = open("input.data").read().strip().splitlines()
datax = """
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
""".strip().splitlines()

monkeys = {}
for monkey in data:
    name, operation = monkey.split(": ")
    if " " in operation:
        monkeys[name] = {"name": name, "calc": operation}
    else:
        monkeys[name] = {"name": name, "value": int(operation)}


def yell_or_work_out(monkey):
    # print("Monkey:", monkey["name"])
    if "value" in monkey:
        monkey["v"] = monkey["value"]
        return monkey["value"]

    calc = monkey["calc"].split(" ")
    operand = calc.pop(1)

    numbers = []
    for next_monkey in calc:
        numbers.append(yell_or_work_out(monkeys[next_monkey]))

    result = None
    if operand == "+":
        result = numbers[0] + numbers[1]
    if operand == "-":
        result = numbers[0] - numbers[1]
    if operand == "*":
        result = numbers[0] * numbers[1]
    if operand == "/":
        result = int(numbers[0] / numbers[1])
    if operand == "=":
        result = numbers[0] == numbers[1]
    # else:
    #    print("WHAT", calc, numbers)
    #    input()

    # print(numbers, operand, result)
    # input()
    monkeys[monkey["name"]]["v"] = result
    return result


if True:
    root = monkeys["root"]
    result = yell_or_work_out(root)
    print("Part 1:", result)

    monkeys = {}
    for monkey in data:
        name, operation = monkey.split(": ")
        if " " in operation:
            monkeys[name] = {"name": name, "calc": operation}
        else:
            monkeys[name] = {"name": name, "value": int(operation)}

root = monkeys["root"]
root["calc"] = root["calc"].replace("+", "=")
i = 3759569926186  # deduced by finding the diff and increasing big, reducing for every iteration to get closer to a==b
while True:
    monkeys["humn"]["value"] = i
    if yell_or_work_out(root):
        print("Part 2:", i)
        break
    else:
        # print("humn", i, monkeys["pppw"]["v"], monkeys["sjmn"]["v"])
        a = monkeys["jdqw"]["v"]
        b = monkeys["nrrs"]["v"]
        delta = a - b
        print("humn", i, a, b, "delta", delta)
        input()
    # i += 1561030368458
    i += 1

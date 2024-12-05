from collections import defaultdict
from math import prod

data = open("input.data").read().strip().splitlines()


def calc(old):
    if old == "old * old":
        return lambda x: x * x

    old, op, num = old.split(" ")
    num = int(num)
    return lambda x: [x + num, x * num][op == "*"]


def get_monkeys():
    global data
    monkeys = []
    monkey = None
    for line in data:
        line = line.strip()
        if line.startswith("Monkey"):
            monkey = {"items": [], "operation": "", "test": 1, True: None, False: None}
            monkeys.append(monkey)

        if line.startswith("Starting items:"):
            items = line.split(": ")[-1].split(",")
            for item in items:
                monkey["items"].append(int(item))

        if line.startswith("Test:"):
            monkey["test"] = int(line.split("by ")[-1])

        if line.startswith("If true:"):
            monkey[True] = int(line.split("to monkey ")[-1])

        if line.startswith("If false:"):
            monkey[False] = int(line.split("to monkey ")[-1])

        if line.startswith("Operation:"):
            monkey["operation"] = calc(line[17:])

    return monkeys


def monkey_business(active: defaultdict) -> int:
    mb = sorted(active.values())
    return mb[-1] * mb[-2]


def part1():
    active = defaultdict(int)
    monkeys = get_monkeys()
    for i in range(20):
        for n, monkey in enumerate(monkeys):
            for item in monkey["items"]:
                active[n] += 1
                new = monkey["operation"](item) // 3
                monkeys[monkey[new % monkey["test"] == 0]]["items"].append(new)
            monkey["items"] = []

    print("Part 1:", monkey_business(active))


def part2():
    active = defaultdict(int)
    monkeys = get_monkeys()
    mod = prod(m["test"] for m in monkeys)

    for i in range(10000):
        for n, monkey in enumerate(monkeys):
            for item in monkey["items"]:
                active[n] += 1
                new = monkey["operation"](item) % mod
                monkeys[monkey[new % monkey["test"] == 0]]["items"].append(new)
            monkey["items"] = []

    print("Part 2:", monkey_business(active))


part1()
part2()

data = open("input.data").read().strip().split("\n")

testdata = """
1 + 2 * 3 + 4 * 5 + 6 = 71
(2 * 3) + 2 = 8
1 + (2 * 3) + (4 * (5 + 6)) = 51
2 * 3 + (4 * 5) = 26
5 + (8 * 3 + 9 + 3 * 4 * 3) = 437
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) = 12240
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 = 13632
""".strip().split("\n")

testdata2 = """
1 + 2 * 3 + 4 * 5 + 6 = 231
1 + (2 * 3) + (4 * (5 + 6)) = 51
2 * 3 + (4 * 5) = 46
5 + (8 * 3 + 9 + 3 * 4 * 3) = 1445
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) = 669060
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 = 23340
""".strip().split("\n")

class Calculator():
    index: int
    result: int
    operator: str
    number: list
    equation: str
    processed: list
    groups: list

    def __init__(self):
        self.ac()

    @property
    def current(self) -> int:
        if not self.number:
            return 0
        return int("".join(self.number))

    def ac(self):
        self.index = 0
        self.result = 0
        self.number = []
        self.equation = ""
        self.processed = []
        self.groups = []

    def c(self):
        self.number = []

    def accumulate(self, group: list):
        group.append(self.current)
        self.c()

    def calculate(self, equation: str, advanced: bool = False) -> int:
        self.ac()
        self.equation = equation
        group = []
        self.result = self.execute(group, advanced=advanced)
        return self.result

    def execute(self, group: list, advanced: bool = False) -> int:
        result = 0
        while self.index < len(self.equation):
            char = self.equation[self.index]
            self.index += 1

            if char.isdigit():
                self.number.append(char)

            if char == " ":
                if not self.number:
                    continue

                self.accumulate(group)

            if char in ("+", "*"):
                group.append(char)

            if char == "(":
                new_group = []
                group.append(new_group)
                result = self.execute(new_group, advanced=advanced)

            if char == ")":
                if self.number:
                    self.accumulate(group)
                return result

        if self.number:
            self.accumulate(group)

        self.operator = "+"
        output = []
        while group:
            part = group.pop(0)
            while self.has_child(part):
                part = self.calculate_parenthesis(part, advanced=advanced)

            if part in ("+", "*"):
                self.operator = part
                output.append(part)
                continue

            elif type(part) == type([]):
                if advanced:
                    output.append(self.calc_sums(part))
                else:
                    part = self.process_parenthesis(part)
            else:
                output.append(part)

            if not advanced:
                if self.operator == "*":
                    result *= part
                else:
                    result += part

        if advanced:
            return self.calc_sums(output)
        return result

    def has_child(self, part) -> bool:
        if part in ("+", "*"):
            return False
        if type(part) == type(0):
            return False
        return len(list(filter(lambda x: type(x) == type([]), part))) > 0

    def calculate_parenthesis(self, part: list, advanced: bool = False) -> list:
        for i, p in enumerate(part):
            if type(p) == type([]):
                if not self.has_child(p):
                    part[i] = self.calc_sums(p) if advanced else self.process_parenthesis(p)

        return part

    def process_parenthesis(self, equation: list) -> int:
        result = equation[0]
        operator = "+"
        for item in equation[1:]:
            if item in ("+", "*"):
                operator = item
                continue

            if operator == "*":
                result *= item
            else:
                result += item

        return result

    def calc_sums(self, equation: list) -> int:
        output = []

        sum = 0
        for index in range(len(equation)):
            eq = equation[index]
            if eq == "+":
                continue

            if eq == "*":
                output.append(sum)
                sum = 0
                continue

            sum += eq

        output.append(sum)

        result = output[0]
        for num in output[1:]:
            result *= num

        return result

#
#

calculator = Calculator()

def part1(data: list):
    result = 0
    for line in data:
        #answer = None
        if line.startswith("#"):
            continue
        if line.find(" = ") != -1:
            line, answer = line.split(" = ")

        sum = calculator.calculate(line)
        result += sum

        #if answer:
        #    print("Calculated   :", sum)
        #    print("Actual answer:", answer, "==", int(answer) == sum)

    print("Part 1:", result)

def part2(data: list):
    result = 0
    for line in data:
        #answer = None
        if line.startswith("#"):
            continue
        if line.find(" = ") != -1:
            line, answer = line.split(" = ")

        sum = calculator.calculate(line, advanced=True)
        result += sum

        #if answer:
        #    print()
        #    print("Calculated   :", sum)
        #    print("Actual answer:", answer, "==", int(answer) == sum)

    print("Part 2:", result)

part1(data)
part2(data)


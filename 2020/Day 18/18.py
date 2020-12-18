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
#1 + 2 * 3 + 4 * 5 + 6 = 231
1 + (2 * 3) + (4 * (5 + 6)) = 51
#2 * 3 + (4 * 5) = 46
#5 + (8 * 3 + 9 + 3 * 4 * 3) = 1445
#5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) = 669060
#((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 = 23340
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

    def calculate(self, equation: str) -> int:
        self.ac()
        self.equation = equation
        group = []
        self.result = self.execute(group)
        return self.result

    def execute(self, group: list):
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
                result = self.execute(new_group)

            if char == ")":
                if self.number:
                    self.accumulate(group)
                return result

        if self.number:
            self.accumulate(group)

        print("< GROUP", group)
        self.operator = "+"
        output = []
        while group:
            part = group.pop(0)
            #print(">", part, "Yes" if self.has_child(part) else "")
            if self.has_child(part):
                #print("CALC >", part)
                part = self.calculate_parenthesis(part)
                output.append(part)
                print("< CL =", part)

            if part in ("+", "*"):
                self.operator = part
                output.append(part)
                continue

            elif type(part) == type([]):
                part = self.process_parenthesis(part)
                #print("???", part, self.operator, result)
            else:
                output.append(part)

            if self.operator == "*":
                result *= part
            else:
                result += part

        print("OUT", output)
        return result

    def has_child(self, part) -> bool:
        if part in ("+", "*"):
            return False
        if type(part) == type(0):
            return False
        return len(list(filter(lambda x: type(x) == type([]), part))) > 0

    def calculate_parenthesis(self, part: list) -> list:
        for i, p in enumerate(part):
            if type(p) == type([]):
                if not self.has_child(p):
                    part[i] = self.process_parenthesis(p)

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

#
#

calculator = Calculator()

def part1(data: list):
    result = 0
    for line in data:
        answer = None
        if line.startswith("#"):
            continue
        if line.find(" = ") != -1:
            line, answer = line.split(" = ")

        #print()
        #print("----------------")
        print(line)
        sum = calculator.calculate(line)
        result += sum

        if answer:
            print("Calculated   :", sum)
            print("Actual answer:", answer, "==", int(answer) == sum)

    print("Part 1:", result, result == 45840336521334)

part1(data)
#part1(testdata2)


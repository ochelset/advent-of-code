data = open("input.data").read().strip().splitlines()

cycles = 0
strength = []
x = 1
screen = ""


def check_signal():
    if (cycles + 20) % 40 == 0 or cycles == 20:
        strength.append(x * cycles)


def render():
    global screen
    pos = cycles % 40
    if pos == 0:
        screen += "\n"

    screen += ".#"[abs(pos - x) <= 1]


for line in data:
    if line == "noop":
        render()
        cycles += 1
        check_signal()
    else:
        render()
        cycles += 1
        value = int(line.replace("addx ", ""))
        check_signal()
        render()
        cycles += 1
        check_signal()
        x += value

    if cycles == 220:
        print("Part 1:", sum(strength))

    if cycles % 40 == 0:
        print(screen)

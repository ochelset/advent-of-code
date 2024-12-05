import math

inputdata = open("input.data").read().strip().splitlines()

TARGET_LOW = 17
TARGET_HIGH = 61

class Bot:
    def __init__(self, value: int):
        self.chips = {value}

    def __repr__(self):
        return "<BOT %s>" % self.chips

    @property
    def is_ready(self):
        return len(self.chips) >= 2

    def add(self, value: int):
        self.chips.add(value)

    def values(self) -> [int]:
        return sorted(self.chips)

bots = {}
outputs = {}
p1 = None

while True:
    for line in inputdata:
        if line.startswith("value"):
            line = line.replace("value", "").replace(" goes to bot", "").strip().split(" ")
            value = int(line[0])
            bot_id = int(line[1])
            if bot_id not in bots:
                bots[bot_id] = Bot(value)
            else:
                bots[bot_id].add(value)
        else:
            line = line[3:].replace("gives low to ", "").replace("and high to ", "").strip().split(" ", 1)
            bot_id = int(line.pop(0))
            if bot_id in bots and bots[bot_id].is_ready:
                low, high = bots[bot_id].values()

                if not p1 and low == TARGET_LOW and high == TARGET_HIGH:
                    p1 = bot_id

                for value in [low, high]:
                    line = line.pop(0).split(" ", 2)
                    target = line.pop(0)
                    target_id = int(line.pop(0))

                    if target == "bot":
                        if target_id not in bots:
                            bots[target_id] = Bot(value)
                        else:
                            bots[target_id].add(value)
                    elif target == "output":
                        outputs[target_id] = value

    if 0 in outputs and 1 in outputs and 2 in outputs:
        break

print("Part 1:", p1)
print("Part 2:", math.prod([outputs[0], outputs[1], outputs[2]]))

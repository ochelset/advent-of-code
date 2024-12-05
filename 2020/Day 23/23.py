class CupsGame():
    index: int
    cups: [int]
    current: int
    moves: int
    lowest: int
    highest: int
    count: int

    def __init__(self, order: str):
        self.index = 0
        self.cups = [int(n) for n in order]
        self.current = self.cups[0]
        self.moves = 0
        self.lowest = min(self.cups)
        self.highest = max(self.cups)
        self.count = len(self.cups)


    def add_cups(self, highest: int):
        for n in range(self.highest + 1, highest + 1):
            self.cups.append(n)
        self.highest = highest
        self.count = len(self.cups)


    def normalize(self):
        self.index = self.cups.index(self.current)
        for n in range(self.index):
            cup = self.cups.pop(0)
            self.cups.append(cup)


    def denormalize(self):
        for n in range(self.index):
            cup = self.cups.pop()
            self.cups.insert(0, cup)

        self.cups = self.cups[:self.count]


    def cup_order(self) -> str:
        index = self.cups.index(1)
        output = self.cups[:]
        for n in range(index):
            cup = output.pop(0)
            output.append(cup)

        return "".join([str(n) for n in output[1:]])


    def get_destination(self, picked_up: [int]) -> int:
        destination = self.current
        while destination in picked_up or destination == self.current:
            destination -= 1
            if destination < self.lowest:
                destination = self.highest

        return destination


    def pick_up(self) -> [int]:
        picked_up = []
        for n in range(3):
            picked_up.append(self.cups.pop(1))
        return picked_up

    def move(self):
        self.moves += 1

        self.normalize()
        picked_up = self.pick_up()
        destination = self.get_destination(picked_up=picked_up)
        destination_index = self.cups.index(destination)

        while picked_up:
            self.cups.insert((destination_index + 1) % self.count, picked_up.pop())

        self.denormalize()

        self.current = self.cups[(self.index + 1) % self.count]


def part1(cups: str):
    game = CupsGame(cups)
    while game.moves < 100:
        game.move()
    print("Part 1:", game.cup_order())

def part2(cups: str):
    game = CupsGame(cups)
    game.add_cups(1000000)
    while game.moves < 100:
        game.move()
    #print("Part 2:", game.cup_order())

part1("871369452")
#part2("389125467")

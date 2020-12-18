data = [10,16,6,0,1,17]

testdata = [3,1,2]


class Game():
    round: int
    starting_numbers: int
    data: list
    memory: dict
    spoken: list

    def __init__(self, data: list):
        self.round = 0
        self.data = data
        self.memory = {}
        self.spoken = []
        self.starting_numbers = len(self.data)

    def speak(self) -> int:
        self.round += 1
        number = self.data.pop(0) if self.data else self.spoken[-1]

        #print("Got", number, self.data)
        #print("Round >", self.round, self.spoken, "=", number)
        if self.round > self.starting_numbers:
            spoken = 0
            if number in self.memory:
                spoken = self.memory[number][-1]

            #print("SPOKEN", spoken, number in self.memory)
            if len(self.memory[number]) == 1:
                #print("First", number)
                number = 0
            else:
                #print("MEM", number, "=", self.memory[number])
                number = abs(spoken - self.memory[number][-2])

        if number not in self.memory:
            self.memory[number] = []

        self.memory[number].append(self.round)
        if len(self.memory[number]) > 2:
            self.memory[number].pop(0)

        self.spoken.append(number)

        return number

    def play(self, target: int):
        while True:
            number = self.speak()
            if self.round == target:
                print("Round", self.round, ":", number)
                break

game = Game(data[:])
game.play(2020)

game = Game(data[:])
game.play(30000000)

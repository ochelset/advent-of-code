"""
"""

class Reindeer:
    def __init__(self, details: str):
        name, speed, fly_time, rest_time = details.split(" ")

        self.name = name
        self.speed = int(speed)
        self.fly_time = int(fly_time)
        self.rest_time = int(rest_time)
        self.points = 0

    def __repr__(self):
        return "<Reindeer %s at %s km, %s points>" % (self.name, self.distance_traveled(), self.points)

    def distance_traveled(self) -> int:
        fly_and_rest_time = self.fly_time + self.rest_time

        traveled_rounds = epoch // fly_and_rest_time
        remainder = epoch % fly_and_rest_time

        distance = self.fly_time * traveled_rounds
        distance += min(remainder, self.fly_time)
        return distance * self.speed

    def point(self):
        self.points += 1
#
#

def parse(data: [str]):
    for line in data:
        individual = Reindeer(line.replace("can fly ", "")
                            .replace("km/s for ", "")
                            .replace("seconds, but then must rest for ", "")
                            .replace(" seconds.", ""))
        reindeer.append(individual)

epoch = 2503
reindeer: [Reindeer] = []

inputdata = open("input.data").read().strip().splitlines()
parse(inputdata)

#winner = max(map(lambda reindeer: reindeer.distance_traveled(), reindeers))
winner = max(reindeer, key=lambda individual: individual.distance_traveled())
print("Part 1: %s at %s km." % (winner.name, winner.distance_traveled()))

for t in range(2503):
    epoch = t + 1
    winner = max(reindeer, key=lambda individual: individual.distance_traveled())
    round_winner_distance = winner.distance_traveled()

    for individual in filter(lambda individual: individual.distance_traveled() == round_winner_distance, reindeer):
        individual.point()

winner = max(reindeer, key=lambda reindeer: reindeer.points)
print("Part 2: %s with %s points" % (winner.name, winner.points))

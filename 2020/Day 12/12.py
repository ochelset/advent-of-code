import math

class Ferry():
    bearing = 90
    heading = "E"
    position = [0, 0]
    waypoint = None

    def __init__(self):
        self.bearing = 90
        self.heading = "E"
        self.position = [0, 0]
        self.waypoint = None


    def set_waypoint(self, x: int, y: int):
        self.waypoint = (x, y)

    def turn(self, to: str, value: int):
        if to == "R":
            self.bearing += value
        else:
            self.bearing -= value

        if self.bearing >= 360:
            self.bearing -= 360
        if self.bearing < 0:
            self.bearing += 360

        self.heading = {
            0: "N",
            90: "E",
            180: "S",
            270: "W"
        }[self.bearing]


    def rotate_waypoint(self, direction: str, degrees: int):
        if direction == "R":
            degrees *= -1

        theta = math.radians(degrees)

        cs = math.cos(theta)
        sn = math.sin(theta)
        px = int(round(self.waypoint[0] * cs - self.waypoint[1] * sn))
        py = int(round(self.waypoint[0] * sn + self.waypoint[1] * cs))

        self.waypoint = [px, py]


    def move(self, direction: str, distance: int):
        if direction == "F":
            direction = self.heading

        move = {
            "N": [0, 1],
            "S": [0, -1],
            "E": [1, 0],
            "W": [-1, 0]
        }[direction]

        self.position[0] += move[0] * distance
        self.position[1] += move[1] * distance


    def move_waypoint(self, to: str, value: int):
        if to == "F":
            self.position = [self.position[0] + self.waypoint[0] * value, self.position[1] + self.waypoint[1] * value]
            return

        move = {
            "N": [0, 1],
            "S": [0, -1],
            "E": [1, 0],
            "W": [-1, 0]
        }[to]
        self.waypoint = [self.waypoint[0] + move[0] * value, self.waypoint[1] + move[1] * value]


    def drive(self, instructions: list):
        for instruction in instructions:
            command, value = [instruction[:1], int(instruction[1:])]

            if self.waypoint:
                if command in "FNSEW":
                    self.move_waypoint(command, value)
                if command in "RL":
                    self.rotate_waypoint(command, value)
            else:
                if command in "FNSEW":
                    self.move(command, value)
                elif command in "RL":
                    self.turn(command, value)

#
#

data = open("input.data").read().strip().split("\n")


def part1(data: list):
    ferry = Ferry()
    ferry.drive(data)
    print("Part 1:", abs(ferry.position[0]) + abs(ferry.position[1]))

def part2(data: list):
    ferry = Ferry()
    ferry.set_waypoint(10, 1)
    ferry.drive(data)
    print("Part 2:", abs(ferry.position[0]) + abs(ferry.position[1]))

part1(data)
part2(data)


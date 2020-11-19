"""
--- Day 15: Oxygen System ---
Out here in deep space, many things can go wrong. Fortunately, many of those things have indicator lights.
Unfortunately, one of those lights is lit: the oxygen system for part of the ship has failed!

According to the readouts, the oxygen system must have failed days ago after a rupture in oxygen tank two;
that section of the ship was automatically sealed once oxygen levels went dangerously low.
A single remotely-operated repair droid is your only option for fixing the oxygen system.

The Elves' care package included an Intcode program (your puzzle input) that you can use to remotely control the repair droid.
By running that program, you can direct the repair droid to the oxygen system and fix the problem.

The remote control program executes the following steps in a loop forever:

Accept a movement command via an input instruction.
Send the movement command to the repair droid.
Wait for the repair droid to finish the movement operation.
Report on the status of the repair droid via an output instruction.
Only four movement commands are understood: north (1), south (2), west (3), and east (4). Any other command is invalid.
The movements differ in direction, but not in distance: in a long enough east-west hallway,
a series of commands like 4,4,4,4,3,3,3,3 would leave the repair droid back where it started.

The repair droid can reply with any of the following status codes:

0: The repair droid hit a wall. Its position has not changed.
1: The repair droid has moved one step in the requested direction.
2: The repair droid has moved one step in the requested direction; its new position is the location of the oxygen system.
You don't know anything about the area around the repair droid, but you can figure it out by watching the status codes.

For example, we can draw the area using D for the droid, # for walls, . for locations the droid can traverse,
and empty space for unexplored locations. Then, the initial state looks like this:



   D


To make the droid go north, send it 1. If it replies with 0, you know that location is a wall and that the droid didn't move:


   #
   D


To move east, send 4; a reply of 1 means the movement was successful:


   #
   .D


Then, perhaps attempts to move north (1), south (2), and east (4) are all met with replies of 0:


   ##
   .D#
    #

Now, you know the repair droid is in a dead end. Backtrack with 3 (which you already know will get a reply of 1 because you already know that location is open):


   ##
   D.#
    #

Then, perhaps west (3) gets a reply of 0, south (2) gets a reply of 1, south again (2) gets a reply of 0, and then west (3) gets a reply of 2:


   ##
  #..#
  D.#
   #
Now, because of the reply of 2, you know you've found the oxygen system! In this example, it was only 2 moves away from the repair droid's starting position.

What is the fewest number of movement commands required to move the repair droid from its starting position to the location of the oxygen system?
ANSWER: 296

--- Part Two ---
You quickly repair the oxygen system; oxygen gradually fills the area.

Oxygen starts in the location containing the repaired oxygen system. It takes one minute for oxygen to spread to all
open locations that are adjacent to a location that already contains oxygen. Diagonal locations are not adjacent.

In the example above, suppose you've used the droid to explore the area fully and have the following map
(where locations that currently contain oxygen are marked O):

 ##
#..##
#.#..#
#.O.#
 ###
Initially, the only location which contains oxygen is the location of the repaired oxygen system. However,
after one minute, the oxygen spreads to all open (.) locations that are adjacent to a location containing oxygen:

 ##
#..##
#.#..#
#OOO#
 ###
After a total of two minutes, the map looks like this:

 ##
#..##
#O#O.#
#OOO#
 ###
After a total of three minutes:

 ##
#O.##
#O#OO#
#OOO#
 ###
And finally, the whole region is full of oxygen after a total of four minutes:

 ##
#OO##
#O#OO#
#OOO#
 ###
So, in this example, all locations contain oxygen after 4 minutes.

Use the repair droid to get a complete map of the area. How many minutes will it take to fill with oxygen?

"""

from math import ceil
from random import random
from IntCodeProcessor import IntCodeProcessor

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

DIRECTIONS = {
    NORTH: "North",
    SOUTH: "South",
    WEST: "West",
    EAST: "East"
}

DIRS = [ NORTH, EAST, SOUTH, WEST ]

WALL = 0
MOVED = 1
OXYGEN = 2

MOVEMENTS = {
    NORTH: [WEST, EAST, EAST, WEST, NORTH],
    SOUTH: [EAST, WEST, WEST, EAST, SOUTH],
    WEST: [SOUTH, NORTH, NORTH, SOUTH, WEST],
    EAST: [NORTH, SOUTH, SOUTH, NORTH, EAST]
}

MOVES = [
    [WEST, EAST],
    [NORTH, SOUTH],
    [EAST, WEST],
    [SOUTH, NORTH]
]

# NEW IDEA:
# - start with the basic move (can be random), move to each side to get information about walls
# - if there are walls on both sides of the current position, we can turn left/right depending on what we have already examined

class Droid:

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    @property
    def randomDirection(self):
        return ceil((random() * 4) % 4)

    def __init__(self, data):
        self.position = (0,0)
        self.controller = IntCodeProcessor(data)
        #self.controller.silent = False
        self.output = { (0,0): { "o": "*" }}
        self.direction = NORTH
        self.oxygen = None
        self.filled = {}

    def get(self, position):
        if position in self.output:
            return self.output[position]
        return None

    def explore(self):
        iterations = 0
        visited = {}
        intersections = []
        route = [self.position]
        while True:
            iterations += 1
            visited[self.position] = True

            validMoves = []
            for move in MOVES:
                position = self.position
                self.controller.inputValues = [move[0]]
                position = self.moved(move[0], position)
                status = self.controller.execute()

                representation = { "o": " ", "pos": position }

                if status == WALL:
                    representation["o"] = " "
                    representation[move[0]] = True
                    self.output[position] = representation
                elif status == OXYGEN:
                    self.oxygen = position
                    representation["o"] = "O"
                    representation[move[0]] = True
                    self.output[position] = representation
                    self.position = position
                    self.render()
                    print("FOUND OXYGEN at", position)
                    break
                else:
                    if position not in visited:
                        validMoves.append(move[0])
                    representation["o"] = "."
                    representation[move[0]] = True
                    self.output[position] = representation
                    self.controller.inputValues = [move[1]]
                    self.controller.execute()

            if self.oxygen:
                print("Part 1:", len(route), self.oxygen)
                self.render(False)
                break

            if len(validMoves) == 1:
                self.direction = validMoves.pop()
                self.position = self.moved(self.direction, self.position)
                self.controller.inputValues = [self.direction]
                self.controller.execute()
                route.append(self.direction)
            elif len(validMoves) > 1:
                intersections.append(self.position)
                self.direction = validMoves.pop()
                self.position = self.moved(self.direction, self.position)
                self.controller.inputValues = [self.direction]
                self.controller.execute()
                route.append(self.direction)
            else:
                if len(intersections) > 0:
                    while True:
                        move = route.pop()
                        if move == WEST:
                            move = EAST
                        elif move == EAST:
                            move = WEST
                        elif move == NORTH:
                            move = SOUTH
                        elif move == SOUTH:
                            move = NORTH

                        self.direction = move
                        self.position = self.moved(self.direction, self.position)
                        self.controller.inputValues = [self.direction]
                        self.controller.execute()

                        if self.position == intersections[-1]:
                            intersections.pop()
                            break
                else:
                    print("NO MOVES", validMoves, intersections)
                    break

    def fill(self):
        self.filled = {}
        print(self.output[self.oxygen])
        size = 50
        minutes = 0
        while True:
            newCells = []
            for y in range(size):
                for x in range(size):
                    pos = (x - size // 2, y - size // 2)
                    value = self.output[pos]["o"] if pos in self.output else " "
                    if value not in ".OD":
                        continue

                    if pos in self.filled:
                        west = (pos[0] - 1, pos[1])
                        east = (pos[0] + 1, pos[1])
                        north = (pos[0], pos[1] - 1)
                        south = (pos[0], pos[1] + 1)
                        for adjacent in (west, north, east, south):
                            if not adjacent in self.output:
                                continue
                            if self.output[adjacent]["o"] == "." and adjacent not in self.filled:
                                newCells.append(adjacent)

            for cell in newCells:
                self.filled[cell] = minutes

            print("MINUTES", minutes)
            self.render()
            input()
            minutes += 1
            self.filled[self.oxygen] = 1


    def moved(self, direction, origin):
        x = origin[0] + [0, 0, 0, -1, 1][direction]
        y = origin[1] + [0, -1, 1, 0, 0][direction]
        return (x, y)

    def render(self, showDroid=True):
        size = 50
        for y in range(size):
            output = []
            for x in range(size):
                pos = (x-size//2, y-size//2)
                value = self.output[pos]["o"] if pos in self.output else " "
                if pos == self.position and showDroid:
                    value = "D"
                if pos in self.filled:
                    value = "O"
                output.append(value)
            print(''.join(output))

#
#

data = open("data/15.data").read()
droid = Droid(data)

droid.explore()
droid.fill()

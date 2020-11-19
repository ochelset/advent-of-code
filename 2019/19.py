"""
--- Day 19: Tractor Beam ---
Unsure of the state of Santa's ship, you borrowed the tractor beam technology from Triton. Time to test it out.

When you're safely away from anything else, you activate the tractor beam, but nothing happens.
It's hard to tell whether it's working if there's nothing to use it on. Fortunately,
your ship's drone system can be configured to deploy a drone to specific coordinates and then check whether it's being pulled.
There's even an Intcode program (your puzzle input) that gives you access to the drone system.

The program uses two input instructions to request the X and Y position to which the drone should be deployed.
Negative numbers are invalid and will confuse the drone; all numbers should be zero or positive.

Then, the program will output whether the drone is stationary (0) or being pulled by something (1).
For example, the coordinate X=0, Y=0 is directly in front of the tractor beam emitter, so the drone control program will always report 1 at that location.

To better understand the tractor beam, it is important to get a good picture of the beam itself. For example,
suppose you scan the 10x10 grid of points closest to the emitter:

       X
  0->      9
 0#.........
 |.#........
 v..##......
  ...###....
  ....###...
Y .....####.
  ......####
  ......####
  .......###
 9........##
In this example, the number of points affected by the tractor beam in the 10x10 area closest to the emitter is 27.

However, you'll need to scan a larger area to understand the shape of the beam.
How many points are affected by the tractor beam in the 50x50 area closest to the emitter? (For each of X and Y, this will be 0 through 49.)
ANSWER: 201

--- Part Two ---
You aren't sure how large Santa's ship is. You aren't even sure if you'll need to use this thing on Santa's ship,
but it doesn't hurt to be prepared. You figure Santa's ship might fit in a 100x100 square.

The beam gets wider as it travels away from the emitter; you'll need to be a minimum distance away to fit a square of that size into the beam fully.
(Don't rotate the square; it should be aligned to the same axes as the drone grid.)

For example, suppose you have the following tractor beam readings:

#.......................................
.#......................................
..##....................................
...###..................................
....###.................................
.....####...............................
......#####.............................
......######............................
.......#######..........................
........########........................
.........#########......................
..........#########.....................
...........##########...................
...........############.................
............############................
.............#############..............
..............##############............
...............###############..........
................###############.........
................#################.......
.................########OOOOOOOOOO.....
..................#######OOOOOOOOOO#....
...................######OOOOOOOOOO###..
....................#####OOOOOOOOOO#####
.....................####OOOOOOOOOO#####
.....................####OOOOOOOOOO#####
......................###OOOOOOOOOO#####
.......................##OOOOOOOOOO#####
........................#OOOOOOOOOO#####
.........................OOOOOOOOOO#####
..........................##############
..........................##############
...........................#############
............................############
.............................###########
In this example, the 10x10 square closest to the emitter that fits entirely within the tractor beam has been marked O.
Within it, the point closest to the emitter (the only highlighted O) is at X=25, Y=20.

Find the 100x100 square closest to the emitter that fits entirely within the tractor beam; within that square,
find the point closest to the emitter. What value do you get if you take that point's X coordinate,
multiply it by 10000, then add the point's Y coordinate? (In the example above, this would be 250020.)
ANSWER: 6610984
"""

from IntCodeProcessor import IntCodeProcessor

data = open("data/19.data").read()

BEAM = 1

class DroneSystem:

    def __init__(self, data):
        self.controller = IntCodeProcessor(data)
        self.scanMap = {}

    def scan(self, startingAt=(0,0), width=10, height=10):
        self.startingAt = startingAt
        self.width = width
        self.height = height
        self.scanMap = {}
        for y in range(self.startingAt[1], self.startingAt[1] + self.height):
            line = []
            beamLeft = -1
            beamRight = -1
            for x in range(self.startingAt[0], self.startingAt[0] + self.width):
                reading = self.examine((x, y))
                self.scanMap[(x, y)] = reading
                if reading == 1:
                    line.append('#')
                    if beamLeft == -1:
                        beamLeft = x
                    beamRight = x
                else:
                    line.append('\u00B7')

            print(''.join(line), y, [beamLeft, beamRight], beamRight-beamLeft)

    def examine(self, position):
        self.controller.resetMemory()
        self.controller.instructionPointer = 0
        self.controller.relativeBase = 0
        self.controller.inputValues = list(position)
        return self.controller.execute()

    def findQuadrant(self, size=5):
        y = 0
        run = True
        while y < 5000 and run:
            x = 0
            while x < 5000:
                if system.findBeamQuadrant((x, y), size):
                    return (x, y)
                x += size
            y += size

    def findBeamQuadrant(self, position, size=5):
        scanResult = []
        positions = [position, (position[0]+size-1, position[1]), (position[0]+size-1, position[1]+size-1), (position[0], position[1]+size-1)]
        for pos in positions:
            scanResult.append(self.examine(pos))
        return sum(scanResult) == 4

    def getScanMap(self, position):
        if position[0] < self.width - 1 and position[1] < self.height - 1:
            return (position, self.scanMap[position])
        return (position, -1)

    def render(self):
        counter = 0
        for y in range(self.startingAt[1], self.startingAt[1] + self.height):
            line = []
            for x in range(self.startingAt[0], self.startingAt[0] + self.width):
                if self.scanMap[(x, y)] == 2:
                    line.append('\u25CC')
                else:
                #if self.scanMap[(x, y)] == 1:
                #    counter += 1
                    line.append('#' if self.scanMap[(x, y)] == 1 else '\u00B7')
            print(''.join(line), y)

        #print("Part 1:", counter)

#
#

size = 100
system = DroneSystem(data)
#system.scan(startingAt=(650, 970), width=120, height=120)
#system.scan(width=60, height=80)
quadrant = system.findQuadrant(size=size)
translate = [(-3,-3), (-2,-2), (-1,-2), (-1,0), (0,-1), (-1,-1)]
if quadrant:
    adjusted = True
    while adjusted:
        adjusted = False
        for t in translate:
            pos = (quadrant[0]+t[0], quadrant[1]+t[1])
            #print(pos, t, system.findBeamQuadrant(pos, size))
            if not system.findBeamQuadrant(pos, size):
                continue

            adjusted = True
            quadrant = pos

    for y in range(quadrant[1], quadrant[1]+size):
        for x in range(quadrant[0], quadrant[0]+size):
            system.scanMap[(x, y)] = 2
    #system.render()
    print("Quadrant starts at", quadrant)
    print("Part 2:", 984 + quadrant[0]*10000)
else:
    print("Found no quadrant")

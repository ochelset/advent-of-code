"""
--- Day 1: No Time for a Taxicab ---
Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.

How many blocks away is Easter Bunny HQ?

Your puzzle answer was 242.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?

"""
data = open("input.data").read().strip().split(", ")

def render():
    global visited
    global hq

    WIDTH = max([x[0] for x in visited])
    WIDTH_MIN = min([x[0] for x in visited])
    HEIGHT = max([x[1] for x in visited])
    HEIGHT_MIN = min([x[1] for x in visited])
    for y in range(HEIGHT_MIN, HEIGHT):
        row = []
        for x in range(WIDTH_MIN, WIDTH):
            if (x, y) == (0, 0):
                row.append("@")
                continue

            if hq and (x, y) == (hq[0], hq[1]):
                row.append("X")
                continue
            row.append(" " if (x, y) in visited else ".")

        print("".join(row))
    print()

#

DIRS = [1,1,-1,-1]
santa = (0, 0, 0)
visited = {(0,0)}
hq = False

print("SA", santa)
while len(data):
    step = data.pop(0)
    dir = (santa[2] + (1 if step[0] == "R" else -1)) % 4
    steps = int(step[1:])
    heading = DIRS[dir]

    print(santa, dir, steps, heading)

    move = (0, 0)
    if dir in (1, 3):
        move = (heading, 0)
        #santa = (santa[0] + (heading * steps), santa[1], dir, heading)
    else:
        move = (0, heading)

    for i in range(steps):
        santa = (santa[0]+move[0], santa[1] + move[1], dir)

        if not hq:
            if (santa[0], santa[1]) in visited:
                hq = santa
                #print(hq, visited)
                #input()
            visited.add((santa[0], santa[1]))

    render()

print()
print("Part 1:", abs(santa[0] + santa[1]))
print("Part 2:", abs(hq[0] + hq[1]))

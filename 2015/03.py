"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

Your puzzle answer was 2572.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.


"""

testdata = """
>
^v
^>v<
^v^v^v^v^v
"""

moves = open("data/03.data").read().strip();

log = {(0, 0): 1}

def countVisitedHouses(moves: str) -> int:
    houses = 1
    x = y = 0

    for move in moves:
        if move == ">":
            x += 1
        if move == "<":
            x -= 1
        if move == "^":
            y += 1
        if move == "v":
            y -= 1

        if not (x, y) in log:
            log[(x, y)] = 1
            houses += 1

    return houses

part1 = countVisitedHouses(moves)
print(part1)

#data = testdata.strip().split("\n")
#for moves in data:
#    print(countVisitedHouses(moves))

#for moves in data:
santaMoves = moves[::2]
robotMobes = moves[1::2]

log = {(0, 0): 1}
print(countVisitedHouses(santaMoves) + countVisitedHouses(robotMobes) - 1)

    #print("S", santaMoves)
    #print("R", robotMobes)
    #print(countVisitedHouses(santaMoves))
    #print(countVisitedHouses(robotMobes))
    #print()

"""
--- Day 20: Infinite Elves and Infinite Houses ---
To keep the Elves busy, Santa has them deliver some presents by hand, door-to-door. He sends them down a street with infinite houses numbered sequentially: 1, 2, 3, 4, 5, and so on.

Each Elf is assigned a number, too, and delivers presents to houses based on that number:

The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5, ....
The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10, ....
Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15, ....
There are infinitely many Elves, numbered starting with 1. Each Elf delivers presents equal to ten times his or her number at each house.

So, the first nine houses on the street end up like this:

House 1 got 10 presents.
House 2 got 30 presents.
House 3 got 40 presents.
House 4 got 70 presents.
House 5 got 60 presents.
House 6 got 120 presents.
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.
The first house gets 10 presents: it is visited only by Elf 1, which delivers 1 * 10 = 10 presents. The fourth house gets 70 presents, because it is visited by Elves 1, 2, and 4, for a total of 10 + 20 + 40 = 70 presents.

What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?
"""

inputdata = 36000000

elves = []

def count_presents_at(house: int) -> int:
    counted_presents = 0
    for elf in range(1, house+1):
        if house % elf == 0:
            #print("Elf %s at Ho" % elf, 10 * elf)
            counted_presents += 10 * elf

    return counted_presents

#
#

def get_factors(num: int) -> set[int]:
    """
    Gets the factors for a given house number.
    Here, this determines the elves that visit each house.
    Args:
        num (int): the house number we want to get factors for
    Returns:
        set[int]: The set of factors (which represent elf numbers)
    """
    factors = set()

    # E.g. factors of 8 = 1, 2, 4, 8
    # Iterate from 1 to sqrt of 8, where %=0, i.e. 1 and 2
    # E.g. for i=1, we add factors 1 and 8
    #      for i=2, we add factors 2 and 4
    # Use a set to eliminate duplicates, e.g. if i is 4, we only want one 2
    for i in range(1, (int(num ** 0.5) + 1)):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)

    return factors

def part1():
    house_number = 500000
    presents = 0

    while presents < inputdata:
        presents = count_presents_at(house_number)
        #print("House %s got %s presents" % (house_number, presents))
        #input()
        if presents >= inputdata:
            break

        house_number += 1

    print("Part 1:", house_number)


part1()

while True:
    count_presents_at(9)
    xx = get_factors(9)
    print(13, 13 / 9, 13 / 3, 13 / 1)
    print(xx)
    input()

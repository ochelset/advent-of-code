data = open("input.data").read().strip().split("\n")

test_data = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".strip().split("\n")

xdata = test_data

rocks = set()
width = len(data)
height = len(data[0])

def get_stones():
    stones = set()
    for y in range(height):
        for x in range(width):
            tile = data[y][x]
            if tile == "O":
                stones.add((x, y))
            if tile == "#":
                rocks.add((x, y))
    return stones

def render(stones):
    for y in range(height):
        row = ''
        for x in range(width):
            if (x, y) in rocks:
                row += '#'
            elif (x, y) in stones:
                row += 'O'
            else:
                row += '.'
        print(row)

def tilt(stones, dir=(0,0)):
    while True:
        still = True
        new_stones = set()
        for stone in stones:
            #old_stones.pop(0)
            moved_stone = (stone[0]+dir[0], stone[1]+dir[1])
            # check against #, O and wall
            if moved_stone[0] < 0 or moved_stone[1] < 0 or moved_stone[0] >= width or moved_stone[1] >= height:
                new_stones.add(stone)
                continue

            if moved_stone in rocks or moved_stone in new_stones:
                new_stones.add(stone)
                continue

            if moved_stone in stones:
                new_stones.add(stone)
                continue

            new_stones.add(moved_stone)
            still = False

        #render(stones)

        #print("Still:", still)
        #input()
        if still:
            return new_stones

        stones = new_stones

def score(stones):
    result = 0
    for y in range(height):
        points = height-y
        for stone in stones:
            if stone[1] == y:
                result += points
    return result

if True:
    stones = get_stones()
    stones = tilt(stones, (0, -1))

    print("Part 1:", score(stones))

stones = get_stones()
#cycles = 3
cycles = 1000000000
while cycles:
    cycle = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    for dir in cycle:
        stones = tilt(stones, dir)
    #print(width*"-")
    #print(width*"-")
    #render(stones)
    #input()

    cycles -= 1
    if cycles % 100 == 0:
        print(cycles)
        print("Part 2:", score(stones)) # 84202 < 84328
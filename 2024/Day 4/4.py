data = open("input.data").read().strip().splitlines()
datax = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip().splitlines()

width = len(data[0])
height = len(data)


def find_word(target, pos, dirs):
    global width
    global height

    result = []
    for d in dirs:
        word = ""
        for move in d:
            p = (pos[0] + move[0], pos[1] + move[1])
            if p[0] < 0 or p[0] >= width or p[1] < 0 or p[1] >= height:
                break
            char = data[p[1]][p[0]]
            word += char
        if word == target:
            result.append((pos, d))
    return result


def part1():
    global data

    dirs = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],  # right
        [(0, 0), (-1, 0), (-2, 0), (-3, 0)],  # left
        [(0, 0), (1, 1), (2, 2), (3, 3)],  # down right
        [(0, 0), (1, -1), (2, -2), (3, -3)],  # up right
        [(0, 0), (-1, -1), (-2, -2), (-3, -3)],  # up left
        [(0, 0), (-1, 1), (-2, 2), (-3, 3)],  # down left
        [(0, 0), (0, 1), (0, 2), (0, 3)],  # down
        [(0, 0), (0, -1), (0, -2), (0, -3)]  # up
    ]

    pos = (0, 0)
    words = []

    while pos[1] < height:
        words.extend(find_word("XMAS", pos, dirs))

        pos = (pos[0] + 1, pos[1])
        if pos[0] >= width:
            pos = (0, pos[1] + 1)

    print("Part 1:", len(words))


def part2():
    global data

    pos = (0, 0)
    words = []
    dirs = [
        [(-1, -1), (0, 0), (1, 1)],  # top left - bottom right
        [(-1, 1), (0, 0), (1, -1)],  # bottom left - top right
        [(1, 1), (0, 0), (-1, -1)],  # bottom right - top left
        [(1, -1), (0, 0), (-1, 1)]  # top right - bottom left
    ]

    while pos[1] < height:
        xwords = find_word("MAS", pos, dirs)
        if len(xwords) == 2:
            words.append(xwords)

        pos = (pos[0] + 1, pos[1])
        if pos[0] >= width:
            pos = (0, pos[1] + 1)

    print("Part 2:", len(words))


part1()
part2()

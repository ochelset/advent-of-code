import math

inputdata = open("input.data").read().strip().replace("\n", "")
inputdatax = """
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###""".strip()

enhancement_algorithm = inputdata[:512]
input_image = inputdata[512:].replace("\n", "")

WIDTH = int(math.sqrt(len(input_image)))
HEIGHT = WIDTH

image = set()
for y in range(HEIGHT):
    for x in range(WIDTH):
        index = y * WIDTH + x
        if input_image[index] == "#":
            image.add((x, y))

def enhance(image, iteration=0):
    on = iteration % 2 == 0 if enhancement_algorithm[0] == "#" else True

    enhanced = set()
    min_x = min(x[0] for x in image) - 2
    max_x = max(x[0] for x in image) + 2
    min_y = min(y[1] for y in image) - 2
    max_y = max(y[1] for y in image) + 2
    for p1 in range(min_x, max_x):
        for p2 in range(min_y, max_y):
            pixel = (p1, p2)
            index = ""
            for y in [-1, 0, 1]:
                for x in [-1, 0, 1]:
                    pos = (x+pixel[0], y+pixel[1])
                    index += "1" if (pos in image) == on else "0"

            if enhancement_algorithm[0] == "." and enhancement_algorithm[int(index, base=2)] == "#":
                enhanced.add(pixel)
            if enhancement_algorithm[0] == "#" and (enhancement_algorithm[int(index, base=2)] == "#") != on:
                enhanced.add(pixel)

    return enhanced

def render(image, span=0):
    min_x = min(x[0] for x in image) - span
    max_x = max(x[0] for x in image) + span
    min_y = min(y[1] for y in image) - span
    max_y = max(y[1] for y in image) + span
    for y in range(min_y, max_y):
        row = []
        for x in range(min_x, max_x):
            row.append("#" if (x, y) in image else " ")
        print("".join(row))
    print()

#

answer1 = 0
for n in range(50):
    image = enhance(image, iteration=n)
    if n+1 == 2:
        answer1 = len(image)

answer2 = len(image)
#render(image, 2)

print("Part 1:", answer1)
print("Part 2:", answer2)
#print("Part 1:", len(list(filter(lambda x: x == 1, image.values()))))
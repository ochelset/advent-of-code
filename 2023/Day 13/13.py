import itertools
from collections import Counter

data = open("input.data").read().strip().split("\n\n")

test_data = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".strip().split("\n\n")

def rotated(dataset):
    temp = []
    for x in range(len(dataset[0])):
        row = ''
        for y in range(len(dataset)):
            row += dataset[y][x]
        temp.append(row[::-1])
    return temp

def check_reflection(temp, part2=False) -> int:
    i = 0
    reflection = -1
    while reflection == -1 and i < len(temp)-1:
        above = temp[i]
        below = temp[i+1]
        if above == below:
            reflection = i
            #print("possible reflection line at", i)
            for ya in range(1, i+1):
                above = temp[i-ya]
                if i+1+ya >= len(temp):
                    #print("outofbounds")
                    break

                below = temp[i+1+ya]
                #print('^',i-ya, above)
                #print('v',i+1+ya, below)
                if above != below:
                    reflection = -1
                    # if part2 :
                    #     count_above = Counter(above)
                    #     count_below  = Counter(below)
                    #     if abs(count_above['#'] - count_below['#']) == 1:
                    #         continue
                    break
                #input()
        #input()

        i += 1
    #print("FOUDN", reflection + 1)
    return reflection + 1

def find_reflection(dataset, part2=False):
    reflection = -1
    verti = check_reflection(dataset, part2)
    horiz = 0
    #if not verti:
    temp = rotated(dataset)
    horiz = check_reflection(temp, part2)
    return (horiz, verti)

def smudged(dataset: str, pos):
    result = ''
    #print("SMUDGE", pos)
    #print(dataset)
    for y, line in enumerate(dataset.splitlines()):
        row = [x for x in line]
        if y == pos[1]:
            if row[pos[0]] == "#":
                row[pos[0]] = "."
            else:
                row[pos[0]] = "#"
        result += ''.join(row) + '\n'

    #print("->")
    #print(result)
    #input()
    return result

#
#

xdata = test_data

if False:
    mirrors = []
    for dataset in data:
        mirror = find_reflection(dataset.splitlines())
        mirrors.append(mirror)

    cols = 0
    rows = 0
    for mirror in mirrors:
        cols += mirror[0]
        rows += mirror[1]*100

    print("Part 1:", cols + rows) #p1 33735, p2 38063

if True:
    mirrors = []
    for dataset in data:
        #print(80*'-')
        #print(dataset)
        #print()
        #mirrored = False
        orig = dataset.splitlines()
        orig_mirror = find_reflection(orig)
        new_mirrors = set()
        new_mirrors.add(orig_mirror)
        for y in range(len(orig)):
            for x in range(len(orig[0])):
                temp = smudged(dataset, (x, y))
                mirror = find_reflection(temp.splitlines())
                if mirror != (0,0) and mirror not in new_mirrors: # and mirror != orig_mirror:
                    new_mirrors.add(mirror)
                    #print("smudged", (x,y), "orig was", orig_mirror)
                    #print(temp)
                    #print(new_mirrors)
                    #mirrored = True
                    #print("-> MIRROR", mirror, "smudged", (x, y))
                    #print(temp)
                    #input()
                    #break
            #if mirrored:
                #break
        if len(new_mirrors) > 1:
            new_mirrors.remove(orig_mirror)
            #print("+ORIG", orig_mirror)
        #input()
        mirrors.extend(list(new_mirrors))
        #print(new_mirrors)

    print(mirrors)
    cols = 0
    rows = 0
    for mirror in mirrors:
        cols += mirror[0]
        rows += mirror[1]*100

    print("Part 2:", cols + rows, ">>", 38063) #p1 33735, p2 38063

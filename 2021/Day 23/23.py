inputdata = """
#############
#...........#
###C#A#D#D###
  #B#A#B#C#
  #########
""".strip().splitlines()

inputdata = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
""".strip().splitlines()

ENERGY = { "A":1, "B":10, "C":100, "D":1000 }
ROOMS = { "A": [(3,2), (3,3)], "B": [(5,2), (5,3)], "C": [(7,2), (7,3)], "D": [(9,2), (9,3)] }
burrow = {}
amphipods = []
consumed = 0
WIDTH = 13
HEIGHT = 5

MOVES = [
    ("A", (1,1))
]

def is_home(amphipod: str, pos: (int, int)) -> bool:
    if ROOMS[amphipod][-1] == pos:
        ROOMS[amphipod].pop()
        return True
    return False

def render():
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            if (x, y) not in burrow:
                row.append(" ")
            elif burrow[(x, y)] == 1:
                row.append("#")
            else:
                row.append(".")

        for amphipod in amphipods:
            if amphipod[0][1] == y:
                row[amphipod[0][0]] = amphipod[1]

        print("".join(row))

def step():
    for amphipod in list(filter(lambda x: x[-1] == False, amphipods)):
        print("Move", amphipod)


for y in range(len(inputdata)):
    line = inputdata[y]
    outside = True
    for x in range(len(line)):
        char = line[x]
        if char != " ":
            outside = False
        if char in "ABCD":
            amphipods.append(((x, y), char, ENERGY[char], 0, is_home(char, (x, y))))
        if not outside:
            burrow[(x, y)] = 1 if char == "#" else 0

render()
step()
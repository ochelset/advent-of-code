inputdata = open("input.data").read().strip().splitlines()
inputdata = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""".strip().splitlines()

risk_level_map = []
for line in inputdata:
    risk_level_map.extend([int(x) for x in line])

WIDTH = len(inputdata[0])
HEIGHT = len(inputdata)

def analyze_quadrant(at: (int, int), distance=1):
    total_risk = 0
    for ay in range(-distance, distance+1):
        for ax in range(-distance, distance+1):
            if ax == 0 and ay == 0:
                continue

            pos = (at[0] + ax, at[1] + ay)
            risk_level = risk_level_at(pos)
            if risk_level == 0:
                continue
            total_risk += risk_level
            print("ANALYZED", pos, risk_level)
    print(total_risk)
#def analyze_path_to(pos, target)

def risk_level_at(pos: (int, int)) -> int:
    if pos[0] < 0 or pos[0] >= WIDTH or pos[1] < 0 or pos[1] >= HEIGHT:
        return 0

    return risk_level_map[pos[1] * WIDTH + pos[0]]

def render():
    path = {}
    for coord in lowest_risk:
        path[(coord[0], coord[1])] = coord[2]

    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            if (x, y) in path:
                row.append(" ")
            else:
                row.append(str(risk_level_at((x, y))))

        print("".join(row))

pos = (0, 0)
target = (WIDTH-1, HEIGHT-1)
lowest_risk = []

#analyze_quadrant((5,5))
while pos != target:
    #pos_right = risk_level_at((pos[0] + 1, pos[1]))
    #pos_down = risk_level_at((pos[0] + 1, pos[1] + 1))
    #pos_down_right = risk_level_at((pos[0] + 1, pos[1] + 1))

    #analyze_quadrant(pos, distance=1)

    #print("POS", pos, "RISKS TO MOVE:", pos_right, pos_down, pos_down+pos_down_right)
    #input()
    lowest_risk.append((pos[0], pos[1], risk_level_at(pos)))
    render()

    right = [(1,0), (2,0)]
    down = [(0,1), (0,2)]

    right_risk = 0
    for at in right:
        right_risk += risk_level_at((pos[0]+at[0], pos[1]+at[1]))

    down_risk = 0
    for at in down:
        down_risk += risk_level_at((pos[0]+at[0], pos[1]+at[1]))

    print("R", right_risk)
    print("D", down_risk)
    if right_risk < down_risk:
        pos = (pos[0] + 1, pos[1])
        print("Go right", pos)
    elif down_risk < right_risk:
        pos = (pos[0], pos[1] + 1)
        print("Go down", pos)
    else:
        right_risk = risk_level_at((pos[0]+1, pos[1]))
        down_risk = risk_level_at((pos[0], pos[1]+1))
        print("r", right_risk)
        print("d", down_risk)
        if right_risk < down_risk:
            pos = (pos[0] + 1, pos[1])
            print("go right", pos)
        elif down_risk < right_risk:
            pos = (pos[0], pos[1] + 1)
            print("go down", pos)
        else:
            print("WHAT???")
            input()


    input()


    #pos = (pos[0] + 1, pos[1] + 1)
    #print("NEW", pos)
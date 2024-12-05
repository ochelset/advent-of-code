import math

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

def risk_level_at(pos: (int, int), map) -> int:
    if pos[0] < 0 or pos[0] >= WIDTH or pos[1] < 0 or pos[1] >= HEIGHT:
        return 0

    return map[pos[1] * WIDTH + pos[0]]

def render(map):
    path = {}
    for coord in lowest_risk:
        path[(coord[0], coord[1])] = coord[2]

    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            if (x, y) in path:
                row.append("  ")
            else:
                row.append(str(risk_level_at((x, y), map)).rjust(2, "0"))

        print(" ".join(row))
    print()

def delta(a, b):
  return abs(b[0] - a[0]) +  abs(b[1] - a[1])

def add_distance_from(pos, map):
  for y in range(HEIGHT):
    for x in range(WIDTH):
      d = delta(pos, (x, y))
      map[y*WIDTH+x] += math.floor(d)
      #print(pos, "->", (x, y), "=", d)


pos = (0, 0)
target = (WIDTH-1, HEIGHT-1)
lowest_risk = []


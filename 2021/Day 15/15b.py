from collections import defaultdict
from queue import PriorityQueue

inputdata = open("input.data").read().strip().splitlines()

risk_level_map = []
for line in inputdata:
    risk_level_map.append([int(x) for x in line])

WIDTH = len(inputdata[0])
HEIGHT = len(inputdata)

def dijkstra(graph, start, destination):
    pq = PriorityQueue()
    pq.put((0, start))
    dists = defaultdict(lambda: float('inf'))
    dists[start] = 0

    WIDTH = len(graph[0]) - 1
    HEIGHT = len(graph) - 1

    while not pq.empty():
        dist, current_vertex = pq.get()
        if current_vertex == destination:
            return dist

        if dists[current_vertex] < dist:
            continue

        x, y = current_vertex
        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx > WIDTH or ny < 0 or ny > HEIGHT:
                continue
            new_dist = dist + graph[ny][nx]
            if dists[(nx, ny)] > new_dist:
                dists[(nx, ny)] = new_dist
                pq.put((new_dist, (nx, ny)))

    return None

#

pos = (0, 0)
target = (WIDTH-1, HEIGHT-1)

print("Part 1:", dijkstra(risk_level_map, pos, target))

duplicated_map = []
repeats = 5

for y in range(HEIGHT*repeats):
    row = []
    for x in range(WIDTH*repeats):
        factor = x // WIDTH + y // HEIGHT
        row.append(factor)
    duplicated_map.append(row)

if True:
    for y in range(len(duplicated_map)):
        for x in range(len(duplicated_map[0])):
            duplicated_map[y][x] = duplicated_map[y][x] + risk_level_map[y % HEIGHT][x % WIDTH]
            if duplicated_map[y][x] > 9:
                duplicated_map[y][x] -= 9

target = (len(duplicated_map[0])-1, len(duplicated_map)-1)
print("Part 2:", dijkstra(duplicated_map, pos, target))

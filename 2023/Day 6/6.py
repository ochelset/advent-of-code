import itertools
from functools import reduce

time = [50, 74, 86, 85]
distance = [242, 1017, 1691, 1252]

if True:
    time = [7, 15, 30]
    distance = [9, 40, 200]

def race(time, distance):
    b = []
    s = []
    d = []
    w = []

    for i in range(len(time)):
        t = time[i]
        d = distance[i]
        wins = 0

        #print(80*"-")
        #print("RACE", t, d)

        for j in range(1, t):
            if (t-j) * j > d:
                wins += 1
            #print(j, t-j, (t-j)*j)

        w.append(wins)

    return reduce((lambda x, y: x * y), w)

result_1 = race(time, distance)
print("Part 1:", result_1)

#result_2 = race([71530], [940200])
result_2 = race([50748685], [242101716911252])
print("Part 2:", result_2)
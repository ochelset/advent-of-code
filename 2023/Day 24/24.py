import itertools
from itertools import combinations
from collections import Counter

data = open("input.data").read().strip().split("\n")
test_area = [(200000000000000, 200000000000000), (400000000000000, 400000000000000)]

if True:
    test_data = """
    19, 13, 30 @ -2,  1, -2
    18, 19, 22 @ -1, -1, -2
    20, 25, 34 @ -2, -2, -4
    12, 31, 28 @ -1, -2, -1
    20, 19, 15 @  1, -5, -3
    """.strip().split("\n")

    data = test_data
    test_area = [(7,7), (27, 27)]

hails = []
for line in data:
    p, v = line.split(" @ ")
    pp = p.split(",")
    vv = v.split(",")
    h = { "p": (int(pp[0]), int(pp[1]), int(pp[2])), "v": (int(vv[0]), int(vv[1]), int(vv[2])) }
    hails.append(h)

for a, b in combinations(range(len(data)), 2):
    a = hails[a]
    b = hails[b]

    print(a)
    print(b)

    xstep = 0
    if a["v"][0] < 0:
        xstep = a["p"][0] - test_area[0][0]

    A = (a["p"][0] + a["v"][0] * xstep)
    print(A)

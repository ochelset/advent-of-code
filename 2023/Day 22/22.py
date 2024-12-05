import itertools
from collections import Counter

data = open("input.data").read().strip().split("\n")

test_data = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
""".strip().split("\n")

data = test_data

width = len(data[0])
height = len(data)

bricks = []

for line in data:
    a, b = line.split("~")
    a = [int(x) for x in a.split(",")]
    b = [int(x) for x in b.split(",")]

    print(a, b)

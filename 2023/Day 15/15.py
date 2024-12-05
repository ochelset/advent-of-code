import itertools
from collections import Counter

data = open("input.data").read().strip().split(",")

test_data = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7""".split(",")

xdata = test_data

def hash(inp):
    current = 0
    for char in inp:
        value = ord(char)
        current += value
        current *= 17
        current %= 256
    return current

def find_index(label, box=[]):
    i = 0
    for b in box:
        if b[0] == label:
            return i
        i += 1
    return -1

result = 0
for step in data:
    result += hash(step)

print("Part 1:", result)

boxes = {}
for step in data:
    label = step.replace("=", " ").replace("-", " ").split(" ")[0].strip()
    focal = 0
    operation = "-"
    if "=" in step:
        operation = "="
        focal = int(step.split("=")[1])
    box = hash(label)

    if not box in boxes:
        boxes[box] = []

    if operation == "=":
        exists = find_index(label, boxes[box])
        if exists != -1:
            boxes[box].pop(exists)
            boxes[box].insert(exists, (label, focal))
        else:
            boxes[box].append((label, focal))

    if operation == "-":
        exists = find_index(label, boxes[box])
        if exists != -1:
            boxes[box].pop(exists)

        if len(boxes[box]) == 0:
            del boxes[box]

result = 0
for n in range(256):
    if n in boxes:
        #print("Box", n, boxes[n])
        for i, lens in enumerate(boxes[n]):
            result += (n+1) * (i+1) * lens[1]
            #print(n+1, i+1, lens, "->", (n+1) * (i+1) * lens[1])

print("Part 2:", result)
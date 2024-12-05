inputdata = open("input.data").read().strip().splitlines()
xinputdata = """
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar""".strip().splitlines()

histogram = {}
size = len(inputdata[0])

for i in range(size):
    histogram[i] = {}

for line in inputdata:
    for i in range(size):
        char = line[i]
        if not char in histogram[i]:
            histogram[i][char] = 0
        histogram[i][char] += 1

output = []
modified = []
for i in range(size):
    chars = sorted(list(map(lambda x: (x[1], x[0]), histogram[i].items())))
    output.append(chars[-1][1])
    modified.append(chars[0][1])

print("Part 1:", "".join(output))
print("Part 2:", "".join(modified))


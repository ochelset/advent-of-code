from collections import deque

data = open("input.data").read().strip().splitlines()
datax = """
1
2
-3
3
-2
0
4
""".strip().splitlines()
data = [int(x) for x in data]
enc_data = [x for x in range(len(data))]


def xecode():
    global data, enc_data
    sequence = [(x, data[x]) for x in enc_data]

    for i, num in enumerate(data):
        index = sequence.index((i, num))
        if num == 0:
            continue

        left = sequence[:index]
        right = sequence[index:]
        right.extend(left)
        cur = right.pop(0)
        left = right[:num]
        sequence = right[num:]
        sequence.extend(left)
        sequence.insert(0, cur)

    return [n[1] for n in sequence]


def decode(times=1, secret=1):
    global data
    sequence = [(x, num * secret) for x, num in enumerate(data)]
    rotate_sequence = deque(sequence)

    for t in range(times):
        for code in sequence:
            index = rotate_sequence.index(code)
            rotate_sequence.rotate(-index)
            rotate_sequence.popleft()
            rotate_sequence.rotate(-code[1])
            rotate_sequence.appendleft(code)

    result = [n[1] for n in rotate_sequence]
    zero = result.index(0)
    k1 = (1000 % len(result) + zero) % len(result)
    k2 = (2000 % len(result) + zero) % len(result)
    k3 = (3000 % len(result) + zero) % len(result)
    return sum((result[k1], result[k2], result[k3]))


print("Part 1:", decode())
print("Part 2:", decode(10, 811589153))

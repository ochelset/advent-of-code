data = open("input.data").read().strip()


def compare(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return left - right

    if isinstance(left, list) and isinstance(right, list):
        for n in range(min(len(left), len(right))):
            if result := compare(left[n], right[n]):
                return result
        return len(left) - len(right)

    if isinstance(left, list):
        return compare(left, [right])

    if isinstance(right, list):
        return compare([left], right)


indices = []
pairs = []
for pair in data.split("\n\n"):
    left, right = pair.splitlines()
    left = eval(left)
    right = eval(right)

    pairs.append([left, right])

for i, (left, right) in enumerate(pairs):
    if compare(left, right) < 0:
        indices.append(i + 1)

print("Part 1:", sum(indices))

pairs = []
for pair in data.replace("\n\n", "\n").splitlines():
    pairs.append(eval(pair))

dividers = [[[2]], [[6]]]
for divider in dividers:
    pairs.append(divider)

# bubble sort based on comparison value
n = len(pairs)
swapped = False
for i in range(n - 1):
    for j in range(0, n - i - 1):
        a = pairs[j]
        b = pairs[j + 1]
        if compare(a, b) > 0:
            swapped = True
            pairs[j], pairs[j + 1] = b, a

    if not swapped:
        break

# find decoder key
decoder_key = []
for i, pair in enumerate(pairs):
    if pair in dividers:
        decoder_key.append(i + 1)

print("Part 2:", decoder_key[0] * decoder_key[1])

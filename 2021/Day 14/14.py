inputdata = open("input.data").read().strip().splitlines()

def find_count(pairs) -> int:
    buffer = { polymer_template[-1]: 1 }
    for pair, count in pairs.items():
        if pair[0] not in buffer:
            buffer[pair[0]] = 0
        if pair[1] not in buffer:
            buffer[pair[1]] = 0
        buffer[pair[0]] += count
        #buffer[pair[1]] += count

    high = max(buffer.values())
    low = min(buffer.values())
    return high - low

polymer_template = inputdata.pop(0)
inputdata.pop(0)

rules = {}
for rule in inputdata:
    pair, result = rule.split(" -> ")
    rules[pair] = result

pairs = {}
for j in range(1, len(polymer_template)):
    pair = polymer_template[j-1:j+1]
    output = rules[pair]
    if pair not in pairs:
        pairs[pair] = 0
    pairs[pair] += 1

for i in range(41):
    new_pairs = {}
    for pair, count in pairs.items():
        p1 = pair[0] + rules[pair]
        p2 = rules[pair] + pair[1]
        if p1 not in new_pairs:
            new_pairs[p1] = 0
        if p2 not in new_pairs:
            new_pairs[p2] = 0
        new_pairs[p1] += count
        new_pairs[p2] += count
    pairs = new_pairs.copy()

    if i+1 == 10:
        print("Part 1:", find_count(pairs))
    elif i+1 == 40:
        print("Part 2:", find_count(pairs))

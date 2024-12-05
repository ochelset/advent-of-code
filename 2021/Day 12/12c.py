from collections import defaultdict, deque

inputdata = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
""".strip().splitlines()

E = defaultdict(list)
for line in inputdata:
    a,b = line.strip().split('-')
    E[a].append(b)
    E[b].append(a)

def solve(p1):
    start = ('start', {'start'}, None)
    ans = 0
    Q = deque([start])
    while Q:
        # where we are, which small caves we've visited
        pos, small, twice = Q.popleft()
        #print("PP", pos, small, "|", twice)
        if pos == 'end':
            ans += 1
            continue

        for y in E[pos]:
            if y not in small:
                new_small = set(small)
                if y.lower() == y:
                    new_small.add(y)
                Q.append((y, new_small, twice))
                #print("+Q", (y, new_small, twice))


            #elif y in small and twice is None and y not in ['start', 'end'] and not p1:
            #    Q.append((y, small, y))
    return ans

print("Part 1:", solve(p1=True))
#print(solve(p1=False))
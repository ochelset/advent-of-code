items = [1, 2, 3, 3, 4, 3, 1, 2, 3, 3, 4, 3, 1, 2, 3, 3, 4, 3, 1, 2, 3, 3, 4, 3]
rounds = 1


#  p1 =  1, 2, 3, 3, 4, 3

def render(a, b, i, j):
    row_a = " "
    row_b = "a"
    for n, char in enumerate(a):
        row_a += ["   ", " v "][i == n]
        row_b += " %s," % char
    print(row_a)
    print(row_b)

    row_a = "b"
    row_b = " "
    for n, char in enumerate(b):
        row_a += " %s," % char
        row_b += ["   ", " ^ "][j == n]
    print(row_a)
    print(row_b)


def has_pattern(a: [], min_length=2) -> int:
    middle = len(a) // 2

    if middle < min_length:
        return -1

    aa = a[:middle]
    bb = a[middle:]

    print()
    print("Round", rounds)
    print("1st half:", aa)
    print("2nd half:", bb)

    pattern = []
    i = 0
    start = None
    while i < len(aa):
        j = 0
        ii = i
        while j < len(bb):
            if ii >= len(aa):
                print("PATTERN", i, start, pattern)
                if len(pattern) < min_length:
                    return None
                return pattern

            # render(aa, bb, ii, j)
            # print(">", aa[ii], bb[j])

            if pattern and aa[ii] != bb[j]:
                pattern = []
                # print((ii, j), "a=%s" % aa[ii], "b=%s" % bb[j], "pattern:", pattern, "BREAK")
                start = None
                break

            if aa[ii] == bb[j]:
                if start is None:
                    start = ii
                pattern.append(aa[ii])
                # print("pattern:", pattern)

            # input()
            j += 1
            ii += 1
        i += 1

    return None


acc = [0, 1, 3, 4]
prev_pattern = None
for item in items:
    acc.append(item)
    pattern = has_pattern(acc)
    if pattern:
        print("Curp", pattern)
        print("Prep", prev_pattern)
        input()
    prev_pattern = pattern
    rounds += 1

import math

inputdata = open("input.data").read().strip().splitlines()

example1 = "[[[[1,1],[2,2]],[3,3]],[4,4]]"
example2 = "[[[[[9,8],1],2],3],4]"
inputdata = "[[[[[9,8],1],2],3],4]".strip().splitlines()

def explode(pair, lr, rr):
    return [pair[0] + lr if lr != None else 0, pair[1] + rr if rr != None else 0]

def split(n):
    return [math.floor(n / 2), math.ceil(n / 2)]

def is_pair(r) -> bool:
    return isinstance(r, list) and len(r) == 2 and isinstance(r[0], int) and isinstance(r[1], int)

max_depth = 0
def parse(remain, level=0, value=[], lr=None, rr=None):
    global max_depth

    left_regular = remain[0] if isinstance(remain[0], int) else lr
    right_regular = remain[-1] if isinstance(remain[-1], int) else rr

    print("> ENTERING", level, remain)
    print("LR", left_regular, lr)
    print("RR", right_regular, rr)
    print()

    level += 1
    first = True
    subvalue = []
    for i in range(len(remain)):
        r = remain[i]
        if isinstance(r, int):
            print("P0 ISINT", r)
            subvalue.append(r)
        elif is_pair(r):
            if level == 4 and first:
                first = False

                print("P1 PAIR FIRST EXPLODE", left_regular, r, right_regular, "=>")

                #subvalue = explode(r, left_regular, right_regular)
                if left_regular != None:
                    left_regular += r[0]
                if right_regular != None:
                    right_regular += r[1]
                print("EXPLODED", left_regular, right_regular)
                return (left_regular, right_regular)
                r = 0
                #level -= 1
                #subvalue = explode(r, left_regular, right_regular)
                #subvalue.extend(remain[i+1:])
                #level -= 1
                #return subvalue
            else:
                print("P1 PAIR", r)
                subvalue.append(r)

        if isinstance(r, list):
            print("P2", level, i, r)
            x = parse(r, level, subvalue, left_regular, right_regular)
            if isinstance(x, tuple):
                print("EXPLODED", x, left_regular, right_regular)
            subvalue.append(x)
        #input(">")
    print("< LEAVING", level, subvalue, [left_regular, right_regular])
    level -= 1
    input()
    return subvalue

for line in inputdata:
    print(line)
    output = parse(eval(line), 0)
    print(output)

print("MAX", max_depth)

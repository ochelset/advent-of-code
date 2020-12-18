import math
from time import time as ts

data = open("input.data").read().strip().split("\n")
testdata = """939
7,13,x,x,59,x,31,19""".split("\n")

def find_buses_at(time: int, buses: list):
    line = ""
    for bus in buses:
        if bus == "x":
            line += "."
            continue

        if time % bus == 0:
            line += "D"
        else:
            line += "."

    return line

def leaves_at(bus, time: int) -> bool:
    return True if bus == "x" or time % bus == 0 else False

def part1(data: list):
    eta = int(data[0])
    buses = [int(n) for n in data[1].split(",") if n != "x"]

    print(eta, buses)

    bus_id = 0
    timestamp = 0
    for time in range(eta, eta+100000):
        for bus in buses:
            if time % bus == 0:
                bus_id = bus
                timestamp = time
                break

        if timestamp >= eta:
            break

    wait_time = timestamp - eta
    print("Part 1:", bus_id, timestamp, ">", wait_time, "=", bus_id * wait_time)


def part2(data: list):
    buses = data[1].split(",")
    bus_count = len(buses)

    for index, bus in enumerate(buses):
        buses[index] = int(bus) if bus != "x" else "x"

    xuses = [int(n) for n in data[1].split(",") if n != "x"]
    #highest = max(xuses)
    #lowest = min(xuses)

    p = 1
    for bus in xuses:
        p *= bus

    #print(lowest, highest, p, p / 3, p / lowest, p / highest, p / bus_count)

    time = int(p / 3)
    while True:
        if leaves_at(buses[0], time):
            break

        time += 1

    #print("Start:", time, leaves_at(buses[0], time))

    while True:

        if leaves_at(buses[-1], time + bus_count - 1):
            subsequent = False
            t = time
            for index, bus in enumerate(buses[1:-1]):
                if not leaves_at(bus, t+index+1):
                    break

                if index == bus_count - 3:
                    subsequent = True

            if subsequent:
                print("Part 2:", time)
                break

        time += 1

def partX(data: list):
    buses = data[1].split(",")

    for index, bus in enumerate(buses):
        buses[index] = int(bus) if bus != "x" else "x"

    product = 1
    pattern = []
    highest = 0
    high_index = 0
    for index, bus in enumerate(buses):
        if bus == "x":
            continue
        product *= bus
        pattern.append((bus, index))

    for index, bus in enumerate(pattern):
        if bus[0] > highest:
            high_index = index
            highest = bus[0]

    time = buses[0] + len(buses) - 1 #buses[0]
    time = product // 3

    result = 0
    for index, bus in enumerate(buses):
        if bus == "x":
            continue

        b = product // bus
        p = pow(b, -1 , bus)
        print("A", bus, index, b, p)
        result += (-index) * p * b

    result = result % product
    print("RES:", result)

    target = result
    time = product // 4

    print("start", time, highest, high_index)
    print("patte", pattern)

    #print("STA:", time, time > result)
    step = 1
    while True:
        #print("time is", time, "stepping", step)

        if time % pattern[high_index][0] == 0:
            step = pattern[high_index][0]
            matches = 0
            t = time - pattern[high_index][1]
            #print("Look from", t, time, step, pattern[high_index])
            #input()
            for p in pattern:
                #print("pt", t + p[1])
                if not (t + p[1]) % p[0] == 0:
                    break
                matches += 1

            #print(">", matches, len(pattern))
            #input()
            if matches == len(pattern):
                print("XXX", time - pattern[high_index][1])
                break

        if time > result:
            print("STOP!")
            break

        time += step

    print("T", time - high_index)
    print("R", target)



#part1(data)
t1 = ts()
partX(data)
t2 = ts()

print()
print("Took", (t2-t1)*1000, "ms.")
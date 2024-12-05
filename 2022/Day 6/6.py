data = open("input.data").read().strip()


def find_start(packets, length=4) -> int:
    for i in range(len(data) - length):
        packet = packets[i:i+length]
        check = set()
        for c in packet:
            check.add(c)

        if len(check) == length:
            return i + length

    return -1


start_of_packet = find_start(data)
start_of_message = find_start(data, 14)

print("Part 1:", start_of_packet)
print("Part 2:", start_of_message)


from functools import reduce

inputdata = open("input.data").read().strip()

converted = []
for char in inputdata:
    converted.append("{:04b}".format(int(bytes.fromhex("0"+char).hex(), 16)))
transmission = "".join(converted)

answer = 0

def parse(packet, i=0):
    global answer

    answer += int(packet[:3], base=2)
    type_id = int(packet[3:6], base=2)
    packet = packet[6:]
    i += 6

    if type_id == 4:
        representation = ""
        while True:
            prefix = packet[0]
            value = packet[1:5]
            i += 5
            representation += value
            if prefix == "0":
                return (int(representation, base=2), i)
            packet = packet[5:]
    else:
        indicator = int(packet[0], base=2)
        values = []
        if indicator == 0:
            sub_packet_length = int(packet[1:16], base=2)
            sub_packet = packet[16:16+sub_packet_length]
            i += 16 + sub_packet_length
            while len(sub_packet):
                value, j = parse(sub_packet)
                sub_packet = sub_packet[j:]
                values.append(value)
        else:
            sub_packets_length = int(packet[1:12], base=2)
            sub_packet = packet[12:]
            i += 12
            for n in range(sub_packets_length):
                value, j = parse(sub_packet)
                sub_packet = sub_packet[j:]
                i += j
                values.append(value)

        if type_id == 0:
            return sum(values), i
        elif type_id == 1:
            return reduce(lambda x, y: x * y, values), i
        elif type_id == 2:
            return min(values), i
        elif type_id == 3:
            return max(values), i
        elif type_id == 5:
            return 1 if values[0] > values[1] else 0, i
        elif type_id == 6:
            return 1 if values[0] < values[1] else 0, i
        elif type_id == 7:
            return 1 if values[0] == values[1] else 0, i

evaluated = parse(transmission)[0]
print("Part 1:", answer)
print("Part 2:", evaluated)

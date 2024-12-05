from functools import reduce

inputdata = open("input.data").read().strip()

converted = []
for char in inputdata:
    converted.append("{:04b}".format(int(bytes.fromhex("0"+char).hex(),16)))
remain = "".join(converted)

packet_version = None
packet_id = None

parsed = {}

answer = 0
packet_length = len(remain)
sub_packets_length = 0
packet_operator = None
prev = None

values = []
expressions = []
output = 0

while True:
    if len(remain) == 0 or len(remain) < 10 and int(remain) == 0:
        break

    prev = packet_version

    if packet_version == None:
        if packet_length > 0:
            packet_length -= 3
        packet_version = remain[:3]
        remain = remain[3:]
        answer += int(packet_version, base=2)

    if packet_id == None:
        if sub_packets_length > 0:
            sub_packets_length -= 1
        if packet_length > 0:
            packet_length -= 3
        packet_id = remain[:3]
        remain = remain[3:]
        parsed[packet_version] = { "id": packet_id }

    if packet_id == "100":
        representation = ""
        while True:
            if packet_length > 0:
                packet_length -= 5
            prefix = remain[0]
            value = remain[1:5]
            remain = remain[5:]
            representation += value
            if prefix == "0":
                break

        packet_id = None
        packet_version = None
        values.append(int(representation, base=2))
    else:
        if len(values):
            expressions.append((packet_operator, values))
            values = []
        packet_operator = int(packet_id, base=2)
        packet_id = None
        packet_version = None
        indicator = remain[0]
        size = 15 if indicator == "0" else 11
        if indicator == "0":
            packet_length = int(remain[1:size+1], base=2)
        else:
            sub_packets_length = int(remain[1:size+1], base=2)
        remain = remain[size+1:]

    if (len(remain) == 0 or len(remain) < 10 and int(remain) == 0) or packet_version != prev and packet_operator:
        if packet_operator != None:
            if packet_operator == 0:
                output += sum(values)
            elif packet_operator == 1:
                output += reduce(lambda x, y: x * y, values)
            elif packet_operator == 2:
                output += min(values)
            elif packet_operator == 3:
                output += max(values)
            elif packet_operator == 5:
                output += 1 if values[0] > values[1] else 0
            elif packet_operator == 6:
                output += 1 if values[0] < values[1] else 0
            elif packet_operator == 7:
                output += 1 if values[0] == values[1] else 0

            packet_id = None
            expressions.append((packet_operator, values))
            values = []

if len(values):
    expressions.append(values)
    values = []

print("Part 1:", answer)
#print("V", values, "O", packet_operator)
#print("Part 2:", output, expressions)
